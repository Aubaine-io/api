from typing import Annotated
from datetime import timedelta
from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.dependencies import get_db
from app.schemas.token import Token
from app.services.token import authenticate_user
from app.security.token import create_access_token

ACCESS_TOKEN_EXPIRE_MINUTES = 30

router = APIRouter(
    prefix="/token",
)

@router.post("/")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db)
) -> Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")
