from typing import List
from database import get_db, get_user_collection
from cache import get_cache
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Query
from crud import create_message, get_messages, get_user, create_user
from schemas import MessageCreate, MessageResponse, UserResponse, UserCreate
import logging

logging.basicConfig(level=logging.INFO)



app = FastAPI()

@app.get("/api/v1/messages/", response_model=List[MessageResponse])
async def read_messages(db=Depends(get_db), cache=Depends(get_cache), page: int = Query(1, ge=1), per_page: int = Query(10, ge=1)):
    
    start_index = (page-1) * per_page
    end_index = start_index + per_page
    
    cached_messages = cache.get("messages")

    if cached_messages:
        messages =  [MessageResponse(**msg) for msg in cached_messages]
        messages.sort(key=lambda x: x.created_at, reverse=True)
        return messages[start_index:end_index]
    
    messages = get_messages(db)
    
    messages_to_cache = [message.model_dump() for message in messages]
    
    cache.set("messages", messages_to_cache)
    
    return messages[start_index:end_index]
    

@app.post("/api/v1/message/", response_model=MessageResponse)
async def post_message(message: MessageCreate, db=Depends(get_db), cache=Depends(get_cache)):
    user = get_user(db, message.user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    new_message = create_message(db, message)
    
    cache.delete("messages")
    
    return new_message


@app.post("/api/v1/users/", response_model=UserResponse)
def post_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user(db, user.user_id)
    logging.info(db_user)
    if db_user:
        raise HTTPException(status_code=400, detail="User already registered")
    return create_user(db, user)

@app.get("/api/v1/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/api/v1/messages/count")
async def get_message_count(db: Session = Depends(get_db)):
    count = db.messages.count_documents({})
    return {"total": count}