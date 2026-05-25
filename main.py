from fastapi import FastAPI
from routers.user import router as user_routes
from routers.blog import router as blog_routes
from core.database import Base, engine
from models.user import User
from models.blog import Blog
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(blog_routes)
app.include_router(user_routes)