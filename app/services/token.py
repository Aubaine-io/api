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
    """
    The function `authenticate_user` checks if a user exists in the database and verifies the provided
    password against the hashed password stored for that user.
    
    Args:
      db (Session): The `db` parameter is of type `Session`.
      username (str): The `username` of the user trying to authenticate.
      password (str): The `password` provided by the user trying to authenticate.
    
    Returns:
      If the user exists and the password provided by the user matches the hashed password stored in the
    database for the user, the function will return the user object. Otherwise, it will return False.
    """
    user = get_user_by_username(db, username)

    # Checking if user exist.
    if not user:
        return False
    
    # Checking if the password provided by the user matches the hashed password stored in the database for the user.
    if not verify_password(password, user.hashed_password):
        return False

    return user

async def get_current_user(db: Session, token: Annotated[str, Depends(oauth2_scheme)]):
    """
    The function `get_current_user` validates credentials using a JWT token and retrieves the user from
    the database based on the token's payload.
    
    Args:
      db (Session): The `db` parameter in the `get_current_user` function is of type `Session`.
      token (Annotated[str, Depends(oauth2_scheme)]): A string annotated with a dependency `oauth2_scheme`.
    
    Returns:
      The function `get_current_user` is returning the user object retrieved from the database based on
    the username extracted from the JWT token.
    """

    # Create an HTTP Exception
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        # Decoding the JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[HASH_ALGORITHM])

        # Extracting the "sub" key from the decoded JWT payload
        username: str = payload.get("sub")

        # If the `username` is `None`, it means that the JWT token does not contain a valid username 
        # in its payload. In this case, the function raises a `credentials_exception`
        # This check ensures that the username extracted from the JWT token is not empty
        # or missing, and handles this scenario appropriately by raising an exception.
        if username is None:
            raise credentials_exception

        # Creating a `TokenData` set to the value extracted from the JWT token payload.
        token_data = TokenData(username=username)

    except JWTError:
        raise credentials_exception

    # Get user from `token_data`
    user = get_user_by_username(db, username=token_data.username)

    # Check if user exists
    if user is None:
        raise credentials_exception

    return user
