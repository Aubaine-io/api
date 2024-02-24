import os
from jose import jwt
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
HASH_ALGORITHM = os.getenv("HASH_ALGORITHM")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=HASH_ALGORITHM)
    return encoded_jwt
