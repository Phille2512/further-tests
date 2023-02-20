from fastapi import FastAPI
from app.routes.blog import create_blog_router
from app.clients.db_client import DatabaseClient
from app.config import Config 

def create_application() -> FastAPI:
    config = Config()
    tables = ["user", "liked_post"]
    database_client = DatabaseClient(config, tables)
    user_router = create_blog_router()

    app = FastAPI()
    app.include_router(database_client)
    return app


#from models.base import recreate_postgres_tables
#recreate_postgres_tables()

app = create_application()