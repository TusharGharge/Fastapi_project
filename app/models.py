from sqlalchemy import TIMESTAMP, Boolean, Column, ForeignKey,Integer, String,text
from .database import Base
from sqlalchemy.orm import relationship

class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,nullable=False)
    title=Column(String,nullable=False)
    title=Column(String,nullable=False)
    content=Column(String, nullable=False)
    published=Column(Boolean, server_default='TRUE',default=True)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)
    owner=relationship("Users")


class Users(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,nullable=False)
    email=Column(String,nullable=False,unique=True)
    password=Column(String,nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    phone_number=Column(String,nullable=False,unique=True)

class Vote(Base):
    __tablename__="votes"
    user_id=Column(Integer,ForeignKey("users.id", ondelete="CASCADE"),primary_key=True)
    post_id=Column(Integer,ForeignKey("posts.id", ondelete="CASCADE"),primary_key=True)