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
    return user_data["watched"].append(movie)



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


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

