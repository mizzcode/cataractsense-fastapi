from fastapi import APIRouter, UploadFile, File, Depends
import requests
from sqlalchemy.orm import Session
from datetime import datetime
from app.db.database import SessionLocal
from app.models.models import Prediction

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/predict")
async def predict(file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        files = {'file': (file.filename, await file.read(), file.content_type)}
        response = requests.post("http://127.0.0.1:8000/predict", files=files)

        result_data = response.json()
        print("DEBUG response dari ML API:", result_data)

        # Gunakan key yang sesuai dengan hasil ML API
        if not result_data.get("success"):
            return {
                "status": "fail",
                "message": "API ML gagal memproses"
            }

        result = result_data.get("class_name")
        confidence = result_data.get("confidence")

        # Simpan ke DB
        prediction = Prediction(
            filename=file.filename,
            result=result,
            confidence=confidence,
            timestamp=datetime.utcnow()
        )
        db.add(prediction)
        db.commit()
        db.refresh(prediction)

        return {
            "status": "success",
            "data": {
                "result": result,
                "confidence": confidence
            }
        }

    except Exception as e:
        return {
            "status": "fail",
            "message": str(e)
        }


