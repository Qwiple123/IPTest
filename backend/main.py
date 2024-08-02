from typing import List
from database import get_db
from cache import get_cache
from fastapi import FastAPI, Depends
from crud import create_message, get_messages
from schemas import MessageCreate, MessageResponse




app = FastAPI()

@app.get("/api/v1/messages/", response_model=List[MessageResponse])
async def read_messages(db=Depends(get_db), cache=Depends(get_cache)):
    
    cached_messages = cache.get("messages")
    if cached_messages:
        return [MessageResponse(**msg) for msg in cached_messages]
    
    messages = get_messages(db)
    
    messages_to_cache = [message.dict() for message in messages]
    
    cache.set("messages", messages_to_cache)
    
    return messages
    

@app.post("/api/v1/message/", response_model=MessageCreate)
async def post_message(message: MessageCreate, db=Depends(get_db), cache=Depends(get_cache)):
    new_message = create_message(db, message)
    
    cache.delete("messages")
    
    return new_message