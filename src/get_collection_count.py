from database import *

def get_collection_count(collection_name):
    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        count = collection.count_documents({})
        print(f"The {collection_name} collection has {count} documents.")
    else:
        print(f"The {collection_name} collection does not exist.")