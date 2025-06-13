from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Feedback
from app.schemas.feedback_schema import FeedbackIn
from datetime import datetime

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/feedback")
def submit_feedback(feedback: FeedbackIn, db: Session = Depends(get_db)):
    new_feedback = Feedback(comment=feedback.comment, created_at=datetime.utcnow())
    db.add(new_feedback)
    db.commit()
    return {"message": "Feedback submitted"}
