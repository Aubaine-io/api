from fastapi import FastAPI

import app.database.attributes as Database
from app.routers.user import router as user_router

Database.Base.metadata.create_all(bind=Database.Engine)
app = FastAPI()

app.include_router(user_router)
