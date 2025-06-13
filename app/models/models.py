from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from app.db.database import Base
from pydantic import BaseModel
from typing import Optional

class Prediction(Base):
    __tablename__ = "predictions"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    result = Column(String, nullable=True)
    confidence = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)
    
class PredictionUpdate(BaseModel):
    result: Optional[str]
    confidence: Optional[float]
    
class PredictionResponse(BaseModel):
    id: int
    filename: str
    confidence: float
    result: Optional[str]  # Fixed from 'str | None'
    timestamp: str

    class Config:
        from_attributes = True  # Changed from 'orm_mode'

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    hashed_password = Column(String)

class Feedback(Base):
    __tablename__ = "feedbacks"
    id = Column(Integer, primary_key=True, index=True)
    comment = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)