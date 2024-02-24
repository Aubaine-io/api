from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.attributes import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(256), unique=True, index=True)
    hashed_password = Column(String(256))
    is_active = Column(Boolean, default=True)
