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


# counts the occurance of an object in another object, such as a letter in a
# string or an item in a list. count_what = what you are wanting to count.
# in_what = where that item is, like in a list or a string.
# EXP: to count the number of "dog" in animals_list, call counting("dog", 
# animals_list). It will return an int of the number of times "dog" shows up
# in animals_list.
def counting(count_what, in_what):
    total_count = 0
    for i in in_what:
        if i == count_what:
            total_count += 1

    return total_count

# Goes through the movie dictionaries in the list, which is the value of
# "watched", and creates a list of genres from the "genre" key. Iterates 
# through that list and compares each genre to the current most watched.
# returns the most frequently watched genre. if the "watched" key is associated
# with an empty list instead of movie dictionaries, return None.
def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None

    genre_list = []
    for watched_list in user_data.values():
        for movie in watched_list:
            genre_list.append(movie["genre"])
    
    most_watched_genre = genre_list[0]
    for genre in genre_list:
        if counting(genre, genre_list) > counting(most_watched_genre, 
                                                    genre_list):
            most_watched_genre = genre

    return most_watched_genre

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


def get_friends_unique_watched(user_data):

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

