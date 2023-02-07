from fastapi import APIRouter
from app.schemas.blog import (BlogEntry,CreateBlogResponse)

from app.services.BlogServices import BlogServices

def create_blog_router() -> APIRouter:
    blog_router = APIRouter()
    blog_services = BlogServices()

    @blog_router.post("/blog_entry", response_model=CreateBlogResponse)
    def create_blog_entry(blog_infos: BlogEntry):
        #blog_text=create_blog_text()
        print(blog_infos)
        blog_id = blog_services.create_blog_text(blog_infos)
        created_blog = CreateBlogResponse(Blog_id=blog_id)
        return created_blog


    @blog_router.get("/show_blog/{blog_id}", response_model= BlogEntry)
    def get_blog(blog_id: int): 

        blog_response = blog_services.blog_get(blog_id)

        return blog_response

    return blog_router