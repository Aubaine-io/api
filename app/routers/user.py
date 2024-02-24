from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

import app.schemas.user as UserSchema
from app.dependencies import get_db
import app.library.user as UserLib

router = APIRouter(
    prefix="/users",
)

@router.post("/", response_model=UserSchema.User)
def create_user(user: UserSchema.UserCreate, db: Session = Depends(get_db)):
    db_user = UserLib.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered\n")
    return UserLib.create_user(db=db, user=user)

@router.get("/", response_model=list[UserSchema.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = UserLib.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{user_id}", response_model=UserSchema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = UserLib.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found\n")
    return db_user
