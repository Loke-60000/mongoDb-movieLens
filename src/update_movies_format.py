from database import *

def update_movies_format():
    try:
        collection = db['movies']
        movies_to_update = collection.find({})

        for movie in movies_to_update:
            title = movie['title'].split(' (', 1)[0]
            
            genres = movie['genres'].split('|')
            
            year = int(movie['title'].split('(')[-1].replace(')', ''))

            collection.update_one({'_id': movie['_id']}, {'$set': {'title': title, 'genres': genres, 'year': year}})

        print("Movie documents updated successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")
