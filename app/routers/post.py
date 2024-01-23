from typing import Optional

from sqlalchemy import func
from .. import models,utils
from fastapi import Body, FastAPI, Response,status,HTTPException,Depends,APIRouter
from sqlalchemy.orm import aliased
from ..database import engine,SessionLocal,get_db
from .. import schemas
from . import oauth

from sqlalchemy.orm import Session

router=APIRouter(
    prefix='/posts',tags=['posts']
)

VoteAlias = aliased(models.Vote)
# @router.get("/")
# async def root():
#     return {"message": "Hello Worldfgfdgrd"}



@router.get("/",status_code=status.HTTP_201_CREATED)
async def posts(db: Session = Depends(get_db),current_user:int=Depends(oauth.get_current_user),Limit:int=10,skip:int=0,search:Optional[str]=""):
    post=db.query(models.Post).filter(models.Post.title.contains(search)).limit(Limit).offset(skip).all()
    print(post)
    data = (
        db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
        .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
        .group_by(models.Post.id)
        .filter(models.Post.title.contains(search))
        .limit(Limit)
        .offset(skip)
        .all()
    )
    print(data)
    # results=db.query(models.Post,func.count(models.Vote.post_id).label("Votes")).join(models.Vote,models.Vote.post_id==models.Post.id,isouter=True).group_by(models.Post.id)
  
  
    return {"data":post}




@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.Postdata)
def craeteposts(update_post: schemas.Post,db: Session = Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    # Post_dict=post.dict()
    # Post_dict['id']=randrange(1,10000000)
    # my_posts.append(Post_dict)
    print(current_user.email)
    new_post=models.Post(owner_id=current_user.id,**update_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @router.get("/posts/latest")
# async def post_latest():
#     post=my_posts[len(my_posts)-1]
#     return {"message": post}


@router.get("/{id}",response_model=schemas.Postdata)
async def post(id:int,db: Session = Depends(get_db)):
    post=db.query(models.Post).filter(models.Post.id==id).first()
    # post = (
    #     db.query(models.Post, func.count(models.Vote.post_id).label("votes"))
    #     .join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True)
    #     .group_by(models.Post.id)
    #     .all()
    # )
    print(post)
    if not post:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id not found {id}")
    return post


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    index=db.query(models.Post).filter(models.Post.id==id)
    post=index.first()
    print(post)
    print("current user", current_user)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found : {id} doesn't exist")
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"not authorized to perform action")
    index.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put("/{id}")
def update_post(id:int,update_post:schemas.updatepost,db: Session = Depends(get_db),current_user:int=Depends(oauth.get_current_user)):
    index=db.query(models.Post).filter(models.Post.id==id)
    post=index.first()
    if post==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post is not found : {id} doesn't exist")
    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"not authorized to perform action")
    
    index.update(update_post.dict(),synchronize_session=False)
    db.commit()
    return {"data":"succesful"}

