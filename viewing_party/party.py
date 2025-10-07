# ------------- WAVE 1 --------------------

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

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

# This is the original wrong one:(just leave it here as a reminder)
# def watch_movie(user_data,title):
#     copy_of_user_data = user_data.copy()
#     for movie in copy_of_user_data["watchlist"]:
#         if movie["title"] == title:
#             copy_of_user_data["watchlist"].remove(movie)
#             copy_of_user_data["watched"].append(movie)
#             return copy_of_user_data
    
#     return copy_of_user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            break
        
    return user_data


# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0
    avg_rating = 0

    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        sum_rating += movie["rating"]
    avg_rating = sum_rating / len(user_data["watched"])
    
    return avg_rating

# This is the original wrong one:
# def counting(count_what, in_what):
#     total_count = 0
#     for i in in_what:
#         if i == count_what:
#             total_count += 1

#     return total_count

# def get_most_watched_genre(user_data):
#     if not user_data["watched"]:
#         return None

#     genre_list = []
#     for movie in user_data["watched"]:
#         genre_list.append(movie["genre"])
    
#     most_watched_genre = genre_list[0]
#     for genre in genre_list:
#         if counting(genre, genre_list) > counting(most_watched_genre, 
#                                                     genre_list):
#             most_watched_genre = genre

#     return most_watched_genre

def get_most_watched_genre(user_data):
    genre_frequency = {}
    most_genre = None
    most_count = -1
    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_frequency[genre] = genre_frequency.get(genre, 0) + 1
        
    for genre, count_movie in genre_frequency.items():
        if count_movie > most_count:
            most_count = count_movie
            most_genre = genre
    return most_genre
            
            



# ------------- WAVE 3 --------------------

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
    user_watched = {movie["title"] for movie in user_data["watched"]}
    friends_unique_watched = []
    friends_unique_titles = set()
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            title = movie["title"]
            if (title not in user_watched and title not in friends_unique_titles):
                friends_unique_watched.append(movie)
                friends_unique_titles.add(title)

    return friends_unique_watched

# ------------- WAVE 4 --------------------

# def get_available_recs(user_data):
#     user_watched = set(movie_user["title"] for movie_user in user_data["watched"])
#     recommend = []
#     recs = set()
    
#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             title = movie["title"]
#             if (title not in user_watched and
#                 title not in recs and
#                 movie["host"] in user_data["subscriptions"]):
#                 recommend.append(movie)
#                 recs.add(title)

#     return recommend

def get_available_recs(user_data):
    recommend = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommend.append(movie)
    
    return recommend

# ------------- WAVE 5 --------------------

#function1
# def get_new_rec_by_genre(user_data):
    # most_watched_genre = get_most_watched_genre(user_data)
    # recommended_movie = []
    # recs = set()

    # user_watched = set(movie["title"] for movie in user_data["watched"])

    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         if (movie["title"] not in user_watched and 
    #             movie["genre"] == most_watched_genre and
    #             movie["title"] not in recs):
    #             recommended_movie.append(movie)
    #             recs.add(movie["title"])
    
    # return recommended_movie

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique = get_friends_unique_watched(user_data)
    recommended_movie = []

    for movie in friends_unique:
        if movie["genre"] == most_watched_genre:
            recommended_movie.append(movie)
    
    return recommended_movie
    

# function2 
# def get_rec_from_favorites(user_data):
#     recommendation = []
#     friend_watched = set()
#     for friend in user_data["friends"]:
#         for movie in friend["watched"]:
#             friend_watched.add(movie["title"])

#     for my_movie in user_data["favorites"]:
#         if my_movie["title"] not in friend_watched:
#             recommendation.append(my_movie)
        
#     return recommendation

def get_rec_from_favorites(user_data):
    user_unique = get_unique_watched(user_data)
    recommend = []

    for movie in user_unique:
        if movie in user_data["favorites"]:
            recommend.append(movie)
    
    return recommend

