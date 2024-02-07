from pymongo import MongoClient
from config import mongoUsername, mongoPassword

from database import *



mongo_host = 'localhost'
mongo_port = 27017

client = MongoClient(f"mongodb://{mongoUsername}:{mongoPassword}@{mongo_host}:{mongo_port}/")
db = client['moviesLens']