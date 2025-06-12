from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PredictionResponse(BaseModel):
    id: int
    filename: str
    result: Optional[str] = None
    confidence: float
    timestamp: datetime

    class Config:
        orm_mode = True
        
class PredictionOut(BaseModel):
    id: int
    filename: str
    result: Optional[str]
    confidence: float
    timestamp: datetime
    
    class Config:
        orm_mode = True