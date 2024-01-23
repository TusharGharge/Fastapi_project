from datetime import datetime
from typing import Optional
from pydantic import BaseModel,EmailStr, conint
class Post(BaseModel):
    title:str
    content:str
    published: bool =True

class updatepost(Post):
    pass

class UserOut(BaseModel):
    email: EmailStr
    id:int
    created_at:datetime
    class Config:
        orm_mode = True

class Postdata(Post):
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut
    

    class Config:
        orm_mode = True
    
class Postout(BaseModel):
    Post:Post
    votes:int
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)


class UserLogin(BaseModel):
    email:EmailStr
    password: str
   
class Token(BaseModel):
    access_token:str
    token_type: str

class TokenData(BaseModel):
    id:Optional[str]=None
   