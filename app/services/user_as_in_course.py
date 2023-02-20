from typing import Optional, Tuple
from app.schemas.user import (
    FullUserProfile,
    User,
)
from app.exceptions import UserNotFound
from app.clients.db_client import DatabaseClient
from sqlalchemy import select
from sqlalchemy.sql import func


class UserService:

    def __init__(self, database_client: DatabaseClient):
        self.database_client = database_client

    async def get_all_users_with_pagination(self, start: int, limit: int) -> Tuple[list[FullUserProfile], int]:
        list_of_users = []
        keys = list(self.profile_infos.keys())
        total = len(keys)
        for index in range(0, len(keys), 1):
            if index < start:
                continue
            current_key = keys[index]
            user = await self.get_user_info(current_key)
            list_of_users.append(user)
            if len(list_of_users) >= limit:
                break

        return list_of_users, total

    async def get_user_info(self, user_id: int = 0) -> FullUserProfile:
        
        # liked_post_query and query can be seen as base query

        liked_posts_query = (
            self.database_client.liked_post.user_id,
            func.array_agg(self.database_client.liked_post.post_id).label("liked_posts")
            .groupby(self.database_client.liked_post.c.user_id)
            .where(self.database_client.liked_post.c.id == user_id
            ).cte("liked_post_query")

        query = (
            select(self.database_client.user)
            .join(
                liked_post_query.c.liked_posts,
                liked_post_query.c.user_id == self.database_client.user.c.id
                isouter=True)
            .where(self.database_client.user.c.id == user_id 
            )
        # why do we need to add the next line?
        user = self.database_client.get_first(query)

        if not user:
            raise UserNotFound(user_id=user_id)

        user_info = dict(zip(user.keys(), user))

      
        return FullUserProfile(**user_info)

    async def create_update_user(self, full_profile_info: FullUserProfile, user_id: Optional[int] = None) -> int:
        if user_id is None:
            user_id = len(self.profile_infos)
        liked_posts = full_profile_info.liked_posts
        short_description = full_profile_info.short_description
        long_bio = full_profile_info.long_bio

        self.users_content[user_id] = {"liked_posts": liked_posts}
        self.profile_infos[user_id] = {
            "short_description": short_description,
            "long_bio": long_bio
        }

        return user_id

    async def delete_user(self, user_id: int) -> None:

        if user_id not in self.profile_infos:
            raise UserNotFound(user_id=user_id)

        del self.profile_infos[user_id]
        del self.users_content[user_id]