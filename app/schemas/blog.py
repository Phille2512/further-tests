from pydantic import BaseModel

class Home_information(BaseModel):
    welcome_text: str
    news: str

class BlogEntry(BaseModel):
    header: str
    text: str

class CreateBlogResponse(BaseModel):
    Blog_id: int
