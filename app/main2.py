from fastapi import FastAPI
from app.routes.blog import create_blog_router

def create_application() -> FastAPI:
    user_router = create_blog_router()

    app = FastAPI()
    app.include_router(user_router)
    return app

app = create_application()