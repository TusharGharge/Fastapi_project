from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime,timedelta
from fastapi import APIRouter, Body, FastAPI, Response,status,HTTPException,Depends
from ..database import engine,SessionLocal,get_db

from sqlalchemy.orm import Session

from .. import schemas,models
SECRET_KEY = "09d2ergesgfdgdfgr34erftgrvcv5e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth_schemedata=OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data:dict):
    to_encode=data.copy()
    expire=datetime.utcnow()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token:str,credentional_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms={ALGORITHM})
        token_data: str=payload.get("User_id")

        if id is None:
            raise credentional_exception
        # token_value=schemas.TokenData(id=id)
        # print(token_value)
    except JWTError:
        raise credentional_exception
    return token_data
    
def get_current_user(token:str=Depends(oauth_schemedata),db: Session = Depends(get_db)):
    credentional_exception=HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail=f"could not validate credentials",headers={"WWW-Authenticate": "Bearer"})
    tokendata=verify_access_token(token,credentional_exception)

    user=db.query(models.Users).filter(models.Users.id==tokendata).first()
    return user