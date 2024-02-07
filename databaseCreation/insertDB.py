import json
from pymongo import MongoClient

from config import mongoUsername, mongoPassword

mongo_host = 'localhost'
mongo_port = 27017

client = MongoClient(f"mongodb://{mongoUsername}:{mongoPassword}@{mongo_host}:{mongo_port}/")
db = client['moviesLens']

def import_json_data(filepath, collection_name):
    # Check if collection already exists
    if collection_name in db.list_collection_names():
        print(f"{collection_name} collection already exists. Skipping import.")
        return
    else:
        collection = db[collection_name]
        with open(filepath, 'r') as file:
            for line in file:
                try:
                    data = json.loads(line)
                    collection.insert_one(data)
                except json.JSONDecodeError as e:
                    print(f"An error occurred while parsing JSON: {e}")
        print(f"{collection_name} collection created and data imported.")

import_json_data('json/movielens_movies.json', 'movies')
import_json_data('json/movielens_users.json', 'users')

client.close()
