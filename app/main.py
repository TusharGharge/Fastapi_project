from random import randrange
from typing import Optional
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends
from pydantic import BaseModel
from . import models,utils
from .database import engine,SessionLocal,get_db

from sqlalchemy.orm import Session
from .routers import post, user,auth,vote

from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



my_posts =[{"title":"title of 1", "content":"content of 1 ", "id":1},{"title":"title of 2", "content":"content of 2 ", "id":2}]

def findpost(id):
    for p in my_posts:
        if p["id"]==id:
            return p
def find_index(id):
    for i ,p in enumerate(my_posts):
        if p['id']==id:
            return i

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)




##########################
