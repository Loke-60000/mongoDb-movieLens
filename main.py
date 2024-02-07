import time

from database import *
from src.get_collection_count import *
from src.list_ocupations import *
from src.get_user_occupation import *
from src.count_users_in_age_range import *
from src.count_users_in_certain_occupation import *
from src.get_10_older_users_by_gender_and_occupation import *
from src.insert_one_user import *
from src.add_movie_in_user import *
from src.check_user_by_id import *
from src.update_occupation import *
from src.update_movies_format import *

current_timestamp = int(time.time())
separation=" \n--------------------------------- \n"

print(separation)    
list_occupations('users' )
print(separation)
get_user_occupation('Clifford Johnathan')
print(separation)
count_users_in_age_range(18, 30)
print(separation)
count_users_in_certain_occupation('scientist')
print(separation)
count_users_in_certain_occupation('artist')
print(separation)
get_10_older_users_by_gender_and_occupation('writer', 'F')
print(separation)
insert_one_user(6041, "Amine Amiroune", "M", 31, "scientist")
print(separation)
add_movie_in_user(6041, 573, 3)
print(separation)
check_user_by_id(6041)
print(separation)
update_occupation('programmer', 'developer')
print(separation)
update_movies_format()
print(separation)

client.close()


