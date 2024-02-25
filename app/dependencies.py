from fastapi.security import OAuth2PasswordBearer
from app.database.attributes import SessionLocal

# This instance is used for handling OAuth2 authentication with password flow in FastAPI applications.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    '''
    The function `get_db` returns a database session that is closed after its use.
    '''
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
