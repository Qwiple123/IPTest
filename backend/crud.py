from models import Message
from datetime import datetime
from schemas import MessageCreate






def get_messages(db):
    messages = db.messages.find()
    return [Message(id=str(msg["_id"]), author=msg["author"], content=msg["content"], created_at=msg["created_at"]) for msg in messages]

def create_message(db, message: MessageCreate):
    message_data = message.dict()
    message_data["created_at"] = datetime.now()
    result = db.messages.insert_one(message_data)
    return Message(id=str(result.inserted_id), **message_data)