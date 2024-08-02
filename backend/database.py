from pymongo import MongoClient
from sqlalchemy.ext.declarative import declarative_base
from pymongo.collection import Collection



client = MongoClient("mongodb://mongo:27017/")
db = client["messages_db"]

Base = declarative_base()

def get_user_collection() -> Collection:
    return db.users

def get_db():
    return db