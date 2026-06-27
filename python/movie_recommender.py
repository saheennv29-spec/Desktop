import pandas as pd
movies = pd.read_csv("movies.csv")
genre = input("Enter preferred genre: ")
min_rating = float(input("Enter minimum rating: "))
recommendations = movies[
    (movies["genre"].str.lower() == genre.lower()) &
    (movies["rating"] >= min_rating)
]
if recommendations.empty:
    print("No movies found.")
else:
    print("\nRecommended Movies:\n")
    for _, movie in recommendations.iterrows():
        print(f"{movie['title']} ({movie['rating']})")