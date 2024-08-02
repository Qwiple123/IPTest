from pymongo import MongoClient
from sqlalchemy.ext.declarative import declarative_base




client = MongoClient("mongodb://mongo:27017/")
db = client["messages_db"]

Base = declarative_base()

def get_db():
    return db