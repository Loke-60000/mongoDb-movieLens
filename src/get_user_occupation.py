from database import *

def get_user_occupation(user_name):
    user = db["users"].find_one({"name": user_name})
    if user:
        occupation = user.get("occupation")
        print(f"The occupation of {user_name} is {occupation}.")
    else:
        print(f"No user found with the name {user_name}.")