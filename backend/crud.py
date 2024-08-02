from models import Message, User
from datetime import datetime
from schemas import MessageCreate, UserCreate, UserResponse, MessageResponse
from pymongo.collection import Collection
from sqlalchemy.orm import Session


def get_user(db: Collection, user_id: int) -> UserResponse | None:
    user  = db.users.find_one({"user_id": user_id})
    if user:
        return UserResponse(**user)
    return None

def create_user(db: Collection, user: UserCreate) -> UserResponse:
    user_data = user.model_dump()
    db.users.insert_one(user_data)
    return UserResponse(**user_data)

def get_messages(db):
    messages_cursor = db.messages.find().sort("created_at", -1)
    messages = []
    for msg in messages_cursor:
        msg['id'] = str(msg['_id'])
        msg['created_at'] = msg['created_at'].isoformat()
        messages.append(MessageResponse(**msg))
    return messages

def create_message(db, message: MessageCreate):
    message_data = message.model_dump()
    message_data["created_at"] = datetime.now()
    result = db.messages.insert_one(message_data)
    return Message(id=str(result.inserted_id), **message_data)