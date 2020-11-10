from flask import Flask
from flask_pymongo import pymongo
import app

CONNECTION_STRING = "mongodb+srv://SaumyaDB:Dl2cm2815@cluster0.lztpg.mongodb.net/<dbname>?retryWrites=true&w=majority"

client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('flask_mongodb_atlas')
user_collection = pymongo.collection.Collection(db, 'user_collection')