from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    author: str
    content: str

class MessageResponse(MessageCreate):
    id: str
    content: str
    author: str
    created_at: datetime