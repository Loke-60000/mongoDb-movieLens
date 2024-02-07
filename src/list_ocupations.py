from database import *

def list_occupations(collection_name):
    if collection_name in db.list_collection_names():
        collection = db[collection_name]
        occupations = collection.distinct('occupation')
        print(f"The {collection_name} collection has the following occupations: \n")
        for occupation in occupations:
            print(occupation)
    else:
        print(f"The {collection_name} collection does not exist.")