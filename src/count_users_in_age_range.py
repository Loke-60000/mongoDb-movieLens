from database import *

def count_users_in_age_range(age1, age2):
    count = db["users"].count_documents({"age": {"$gte": age1, "$lte": age2}})
    print(f"There are {count} users between the ages of {age1} and {age2}.")