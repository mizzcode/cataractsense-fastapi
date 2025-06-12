from fastapi import APIRouter, HTTPException, Depends
from app.db.database import SessionLocal
from app.models.models import Prediction
from app.schemas.prediction_schema import PredictionOut
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.schemas.prediction_schema import PredictionResponse


router = APIRouter()

@router.get("/predictions", response_model=List[PredictionResponse])
def get_predictions(db: Session = Depends(get_db)):
    try:
        predictions = db.query(Prediction).all()
        return predictions
    except Exception as e:
        print("ERROR:", str(e))
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/predictions/{id}", response_model=PredictionOut)
def get_prediction(id: int):
    db: Session = SessionLocal()
    prediction = db.query(Prediction).get(id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    return prediction

@router.delete("/predictions/{id}")
def delete_prediction(id: int):
    db: Session = SessionLocal()
    prediction = db.query(Prediction).get(id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")
    db.delete(prediction)
    db.commit()
    return {"message": "Data berhasil dihapus"}

@router.put("/predictions/{id}", response_model=PredictionOut)
def update_prediction(id: int, updated_data: PredictionOut):
    db: Session = SessionLocal()
    prediction = db.query(Prediction).get(id)
    if not prediction:
        raise HTTPException(status_code=404, detail="Data tidak ditemukan")

    prediction.filename = updated_data.filename
    prediction.result = updated_data.result
    prediction.confidence = updated_data.confidence
    db.commit()
    db.refresh(prediction)
    return prediction
