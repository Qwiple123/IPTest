from pydantic import BaseModel
from datetime import datetime

class MessageCreate(BaseModel):
    user_id: int
    content: str

class MessageResponse(MessageCreate):
    id: str
    content: str
    user_id: int
    created_at: datetime
    
class UserCreate(BaseModel):
    user_id: int
    name: str
    nick_name: str
    
class UserResponse(BaseModel):
    user_id: int
    name: str
    nick_name: str

    class Config:
        from_attributes = True