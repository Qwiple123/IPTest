from datetime import datetime
from pydantic import BaseModel, BaseConfig




class Message(BaseModel):
    id: str
    content: str
    author: str
    created_at: datetime
    
    class Config(BaseConfig):
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }