from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.models import Feedback
from app.schemas.feedback_schema import FeedbackCreate, FeedbackOut

router = APIRouter(
    prefix="/api/feedback",
    tags=["Feedback"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FeedbackOut)
def create_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    db_feedback = Feedback(comment=feedback.comment)
    db.add(db_feedback)
    db.commit()
    db.refresh(db_feedback)
    return db_feedback

@router.get("/", response_model=list[FeedbackOut])
def read_feedbacks(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Feedback).offset(skip).limit(limit).all()
