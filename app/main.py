from fastapi import FastAPI

import app.database.attributes as Database
from app.routers.user import router as user_router
from app.routers.token import router as token_router

# Create all the database tables defined in the metadata of the Base class.
Database.Base.metadata.create_all(bind=Database.Engine)

# This instance will be used to define routes, middleware, and other configurations for the API application.
app = FastAPI()

# Adding the routers to the FastAPI application `app`.
app.include_router(token_router)
app.include_router(user_router)
