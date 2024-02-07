from database import *

def count_users_in_certain_occupation(occupation):
    count = db["users"].count_documents({"occupation": occupation})
    print(f"There are {count} users with the occupation {occupation}.")