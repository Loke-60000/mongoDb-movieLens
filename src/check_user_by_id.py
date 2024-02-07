from database import *
import pprint

def check_user_by_id(user_id):
    try:
        user = db["users"].find_one({"_id": user_id})
        pprint.pprint(user)
    except Exception as e:
        print(f"An error occurred: {e}")
