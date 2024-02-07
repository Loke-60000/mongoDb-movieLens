from pymongo import MongoClient
import time
from database import *

def add_movie_in_user(user_id, movieid, rating):
    current_timestamp = int(time.time())

    movie = {
        "movieid": movieid,
        "rating": rating,
        "timestamp": current_timestamp
    }

    result = db["users"].update_one(
        {"_id": user_id, "movies.movieid": {"$ne": movieid}},
        {"$push": {"movies": movie}}
    )

    if result.modified_count > 0:
        print(f"Movie added to user id:{user_id}'s list successfully.")
    else:
        print("No update performed. Please check the user ID or movie ID and try again.")
