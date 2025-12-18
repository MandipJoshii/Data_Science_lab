# 1. Movie Ratings Analyzer
# Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...].
# Compute the average rating, find the highest-rated movie, and list all movies with rating above the average.

# 1. Movie Ratings Analyzer

# 1. Movie Ratings Analyzer

movie_detail = []

print("ENTER MOVIE NAME AND RATING (press ENTER with no name to finish)\n")

while True:
    movie_name = input("ENTER MOVIE NAME: ").strip()

    # ✅ Professional way to end input
    if movie_name == "":
        break

    rating_input = input("ENTER YOUR RATING: ")

    try:
        if "." in rating_input:
            rating = float(rating_input)
        else:
            rating = int(rating_input)
    except:
        print("RATING CANNOT HAVE SPECIAL CHARACTERS OR STRING VALUE")
        continue

    movie_detail.append((movie_name, rating))

print("\nLIST OF MOVIES:", movie_detail)

# -----------------------------
# AVERAGE RATING
# -----------------------------
total_movie = 0

for movie in movie_detail:
    total_movie += movie[1]

average = total_movie / len(movie_detail)
print(f"\nAVERAGE MOVIE RATING: {average}")

# -----------------------------
# HIGHEST RATING
# -----------------------------
highest_rating = movie_detail[0][1]
highest_movie = movie_detail[0][0]

for movie in movie_detail:
    if movie[1] > highest_rating:
        highest_rating = movie[1]
        highest_movie = movie[0]

print(f"HIGHEST RATING: {highest_rating} ({highest_movie})")

# -----------------------------
# MOVIES ABOVE AVERAGE
# -----------------------------
print("\nMOVIES ABOVE THE AVERAGE RATING:")
for m in movie_detail:
    if m[1] > average:
        print(m[0], "-", m[1])




# movie = [
#     {"name":"Fight Club", "rating":8.8},
#     {"name": "The Dark Knight", "rating": 9.1},
#     {"name": "The Lord of the Ring:The Fellowship of the ring", "rating": 9.0},
#     {"name": "Spirited Away", "rating": 8.6},
#     {"name":"WALL.E" , "rating": 8.4},
# ]


#simplest logic
# average_rating = movie["rating"]/5
# highest_rated = movie[0]["rating"]
# print(average_rating)
# print(highest_rated)




#without user input
# highest_rating = movie[0]["rating"]
# total_movie = 0
# for movies in movie:
#     total_movie += movies["rating"]
    
#     if highest_rating < movies["rating"]:
#         highest_rating = movies["rating"]

# average_rating = total_movie/len(movie)

# print("RATING GREATER THAN AVERAGE RATING: \n")
# for m in movie:
#     if m["rating"] > average_rating:
#         print(m["name"] , "-", m["rating"])

        
# print(f"\nAVERAGE RATING: {average_rating}")
# print(f"Highest Rating: {highest_rating}")

