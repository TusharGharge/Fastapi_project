from fastapi import APIRouter, Body, FastAPI, Response,status,HTTPException,Depends
from fastapi.security import OAuth2PasswordRequestForm
from ..database import engine,SessionLocal,get_db
from .. import schemas,models,utils
from . import oauth
from sqlalchemy.orm import Session

router=APIRouter(tags=['Authentication'])


@router.post('/login',response_model=schemas.Token)
def login(user_cred:OAuth2PasswordRequestForm=Depends(), db:Session=Depends(get_db)):
    user=db.query(models.Users).filter(models.Users.email==user_cred.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid credentionals")
    if not utils.verify(user_cred.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"invalid password credentionals")
    #create tokem
    access_token=oauth.create_access_token(data={"User_id":user.id})
    #return token
    return {"access_token":access_token,"token_type":"bearer"}