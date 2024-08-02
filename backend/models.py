from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from bson import ObjectId


class Message(BaseModel):
    id: str
    content: str
    user_id: int
    created_at: datetime
    
    class Config(ConfigDict):
        json_encoders = {
            datetime: lambda dt: dt.isoformat()
        }
        
class User(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    user_id: int
    name: str
    nick_name: str

    class Config:
        arbitrary_types_allowed=True
        populate_by_name = True
        json_encoders = {ObjectId: str}