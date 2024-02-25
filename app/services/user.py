from sqlalchemy.orm import Session

from app.security.user import get_password_hash
from app.models.user import User
import app.schemas.user as UserSchema

def create_user(db: Session, user: UserSchema.UserCreate) -> User:
    """
    The function `create_user` takes user input, hashes the password, creates a new user in the
    database, and returns the created user.
    
    Args:
      db (Session): The `db` parameter is an instance of a database session.
      user (UserSchema.UserCreate): A `user` object matching the UserCreate schemas. 
    
    Returns:
      The function `create_user` is returning the user object `db_user` that was created and
      added to the database.
    """
    # Generating a hashed version of the user's password before storing it in the database.
    hashed_password = get_password_hash(user.password)
    
    # Creating a new instance of the `User` model class with the provided user details.
    db_user = User(
        email=user.email,
        username=user.username,
        hashed_password=hashed_password
    )

    # Adding the newly created user object `db_user` to the current database.
    db.add(db_user)
    # Committing the current transaction to the database.
    db.commit()
    # Refreshing the state of the `db_user` object in the current database.
    db.refresh(db_user)

    return db_user

def get_user_by_id(db: Session, id: int) -> (User | None):
    """
    The function `get_user` retrieves a user from the database based on the provided user ID.
    
    Args:
      db (Session): The `db` parameter is of type `Session`.
      id (int): The id of the user you want.
    
    Returns:
      Returns the user object from the database with the specified `id`.
    """

    # Querying the database to retrieve a specific user based on the provided `user_id`.
    return db.query(User).filter(User.id == id).first()

def get_user_by_email(db: Session, email: str) -> (User | None):
    """
    The function `get_user_by_email` retrieves a user from the database based on their email address.
    
    Args:
      db (Session): The `db` parameter is of type `Session`.
      email (str): The email of the user you want.
    
    Returns:
      Returns the user object from the database whose email matches the `email` parameter.
    """

    # Query operation that retrieves a user from the database whose email matches the email parameter.
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str) -> (User | None):
    """
    The function `get_user_by_username` retrieves a user from the database based on their username.
    
    Args:
      db (Session): The `db` parameter is of type `Session`.
      username (str): The username of the user you want.
    
    Returns:
      Returns the user object from the database whose username matches the `username` parameter.
    """

    # Query operation that retrieves a user from the database whose username matches the username parameter.
    return db.query(User).filter(User.username == username).first()

def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[User]:
    """
    The function `get_users` retrieves a specified number of users from a database session, with
    optional parameters for skipping and limiting the results.
    
    Args:
      db (Session): The `db` parameter is of type `Session`.
      skip (int): The `skip` parameter is the number of records to skip from the beginning of the query
      result before returning the data. Defaults to 0.
      limit (int): The `limit` parameter specifies the maximum number of user records that should be 
      returned from the database query. Defaults to 100.
    
    Returns:
      The function `get_users` returns a list of User objects from the database, starting from the
    `skip` index and returning up to `limit` number of users.
    """

    # Query operation that retrieve a specified number of user records from the database.
    return db.query(User).offset(skip).limit(limit).all()
