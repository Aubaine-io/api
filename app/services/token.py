import os

from dotenv import load_dotenv
from typing import Annotated
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status

from app.dependencies import oauth2_scheme
from app.schemas.token import TokenData
from app.security.user import verify_password
from app.services.user import get_user_by_username

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
HASH_ALGORITHM = os.getenv("HASH_ALGORITHM")

def authenticate_user(db: Session, username: str, password: str):
    user = get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

async def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user_by_username(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user
