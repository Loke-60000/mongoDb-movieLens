from database import *

def insert_one_user(_id, name, gender, age, occupation):
    user = {
        "_id": _id,
        "name": name,
        "gender": gender,
        "age": age,
        "occupation": occupation
    }
    existing_user = db["users"].find_one({"name": name})
    if existing_user:
        print(f"User {name} already exists.")
    else:
        db["users"].insert_one(user)
        print(f"User {name} inserted successfully.")