from typing import Optional
from app.schemas.blog import (
BlogEntry,
CreateBlogResponse)

blog_entries = {0: {"header": "name", 
"text": "blog"}, 
1: {"header": "tonytone", 
"text": "I be jetzt do"}}

class BlogServices:

    def __init__(self):
        pass

    @staticmethod
    def create_blog_text(blog_infos: BlogEntry):
        global blog_entries

        new_blog_id = len(blog_entries)
        # taking the infos from the request
        blog_header = blog_infos.header
        blog_entry = blog_infos.text
        #inserting it to database
        blog_entries[new_blog_id] = {}
        blog_entries[new_blog_id] = {"header": blog_header,'text': blog_entry}

        return new_blog_id #BlogEntry(**blog_entries[new_blog_id])

    @staticmethod
    def blog_get(blog_id: int):
        
        blog_parts = blog_entries[blog_id]

        return BlogEntry(**blog_parts)