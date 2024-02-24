from fastapi import FastAPI

import app.database.attributes as Database
from app.routers.user import router as user_router
from app.routers.token import router as token_router

Database.Base.metadata.create_all(bind=Database.Engine)
app = FastAPI()

app.include_router(token_router)
app.include_router(user_router)
