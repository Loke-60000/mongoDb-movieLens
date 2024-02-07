from database import *

def get_10_older_users_by_gender_and_occupation(occupation, gender):
    users = db["users"].find({"occupation": occupation, "gender": gender}).sort("age", -1).limit(10)
    if gender == "M":
        GenderName = "male"
    else:
        GenderName = "female"
    
    print(f"10 oldest {GenderName}s in the {occupation} occupation: \n")

    for user in users:
        print(f"{user['name']}, Age: {user['age']}")