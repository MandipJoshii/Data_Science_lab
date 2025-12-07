
movie = [
    {"name":"Fight Club", "rating":8.8},
    {"name": "The Dark Knight", "rating": 9.1},
    {"name": "The Lord of the Ring:The Fellowship of the ring", "rating": 9.0},
    {"name": "Spirited Away", "rating": 8.6},
    {"name":"WALL.E" , "rating": 8.4},
]
# average_rating = movie["rating"]/5
# highest_rated = movie[0]["rating"]
# print(average_rating)
# print(highest_rated)


highest_rating = movie[0]["rating"]
total_movie = 0
for movies in movie:
    total_movie += movies["rating"]
    
    if highest_rating < movies["rating"]:
        highest_rating = movies["rating"]

average_rating = total_movie/len(movie)

print("RATING GREATER THAN AVERAGE RATING: \n")
for m in movie:
    if m["rating"] > average_rating:
        print(m["name"] , "-", m["rating"])

        
print(f"\nAVERAGE RATING: {average_rating}")
print(f"Highest Rating: {highest_rating}")

