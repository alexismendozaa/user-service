from sqlalchemy import Column, Integer, String, DateTime
from app.services.db_service import Base
import datetime

class User(Base):
    __tablename__ = "Users"  # Tabla con "U" mayúscula

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    email = Column(String, unique=True, index=True)
    createdAt = Column(DateTime, default=datetime.datetime.utcnow)  # createdAt en camelCase
    updatedAt = Column(DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)  # updatedAt en camelCase
