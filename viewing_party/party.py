# ------------- WAVE 1 --------------------

# If title, genre, and rating are all truthy, return a dictionary with the
# movie data inside. If any of the given arguments are falsy, return None.
def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title, 
            "genre": genre, 
            "rating": rating
            }
        return new_movie
    else:
        return None

# Adds movie to user_data. Each movie is a dictionary, formatted like new_movie.
# user_data is a dictionary with a "watched" key and a value that's a list of
# dictionaries. 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data



# Adds movie to watchlist
def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data


#If a movie is watched , remove it from watchlist to watched
def watch_movie(user_data,title):
    copy_of_user_data = user_data.copy()
    for movie in copy_of_user_data["watchlist"]:
        if movie["title"] == title:
            copy_of_user_data["watchlist"].remove(movie)
            copy_of_user_data["watched"].append(movie)
            return copy_of_user_data
    
    return copy_of_user_data



# ------------- WAVE 2 --------------------
#Function1 solution1
def get_watched_avg_rating(user_data):
    sum_rating = 0
    avg_rating = 0
    for movie in user_data["watched"]:
        sum_rating += movie["rating"]
        avg_rating = sum_rating / len(user_data["watched"])
    
    return avg_rating



# ------------- WAVE 3 --------------------
# Function1 Solution 3: use set to make it simple,time complexity: n^2, space complexity: f * m
def get_unique_watched(user_data):
    friend_watched = set()
    unique_user_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.add(movie["title"])
            
    for movie in user_data["watched"]:
        if movie["title"] not in friend_watched:
            unique_user_watched.append(movie)
    
    return unique_user_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

