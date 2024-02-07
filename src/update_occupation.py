from database import *

def update_occupation(old_occupation, new_occupation):
    collection = db['users']
    users_to_update = collection.find({'occupation': old_occupation})

    updated = False

    for user in users_to_update:
        user_id = user['_id']
        collection.update_one({'_id': user_id}, {'$set': {'occupation': new_occupation}})
        updated = True

    if updated:
        print(f'Occupation "{old_occupation}" updated to "{new_occupation}" for all relevant users.')
    else:
        print(f'No users found with occupation "{old_occupation}" to update.')
