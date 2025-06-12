from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Prediction
from app.schemas.prediction_schema import PredictionOut

router = APIRouter()



