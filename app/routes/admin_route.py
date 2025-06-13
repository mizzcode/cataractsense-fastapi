from fastapi import APIRouter, Depends
from app.db.database import SessionLocal
from app.models.models import Prediction, User, Feedback
from sqlalchemy.orm import Session

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/predictions")
def get_all_predictions(db: Session = Depends(get_db)):
    return db.query(Prediction).all()

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/feedbacks")
def get_all_feedbacks(db: Session = Depends(get_db)):
    return db.query(Feedback).all()
