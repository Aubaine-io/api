from typing import Annotated
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import app.schemas.user as UserSchema
from app.dependencies import get_db, oauth2_scheme
import app.services.user as UserLib

router = APIRouter(
    prefix="/users",
)

@router.post("/", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    db_user_by_email = UserLib.get_user_by_email(db, email=user.email)
    db_user_by_username = UserLib.get_user_by_username(db, username=user.username)
    if db_user_by_email or db_user_by_username :
        raise HTTPException(status_code=400, detail="Email or Username already registered\n")
    return UserLib.create_user(db=db, user=user)

@router.get("/", response_model=list[UserSchema.User])
def read_users(token: Annotated[str, Depends(oauth2_scheme)], skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserLib.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserSchema.User)
def read_user(token: Annotated[str, Depends(oauth2_scheme)], user_id: int, db: Session = Depends(get_db)):
    db_user = UserLib.get_user_by_id(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found\n")
    return db_user
