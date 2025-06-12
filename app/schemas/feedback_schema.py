from pydantic import BaseModel
from datetime import datetime

class FeedbackIn(BaseModel):
    comment: str

class FeedbackCreate(BaseModel):
    comment: str 
    
class FeedbackOut(BaseModel):
    id: int
    comment: str
    created_at: datetime

    class Config:
        orm_mode = True