# 1. IMPORTING LIBRARIES
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# 2.1 Sample Movie Data
movies_data = {
    'MovieID': [1, 2, 3, 4, 5],
    'MovieName': ['Movie A', 'Movie B', 'Movie C', 'Movie D', 'Movie E'],
    'Genre': ['Action', 'Comedy', 'Action', 'Drama', 'Comedy'],
    'Description': ['Action-packed movie with explosions and fights.',
                        'A funny comedy with lots of laughs and humor.',
                        'Thrilling action movie with suspenseful scenes.',
                        'A drama with emotional and touching moments.',
                        'A funny comedy with lots of laughs and humor.']
}

# 2.2 Sample Ratings Data
ratings_data = {
    'UserID': [1, 1, 2, 2, 3],
    'MovieID': [1, 2, 3, 4, 5],
    'Rating': [5, 4, 3, 2, 4],
}

movies_df = pd.DataFrame(movies_data)
ratings_df = pd.DataFrame(ratings_data)

# 3. Merge dataframes to get movie details with ratings
movie_ratings = pd.merge(ratings_df, movies_df, on='MovieID')

# 4. CONTENT-BASED FILTERING

# 4.1 Create a TF-IDF vectorizer to convert genres into numerical features
tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(movies_df['Genre'])

# 4.2 Compute COSINE-SIMILARITY between movies based on TF-IDF vectors
cosine_similarity = linear_kernel(tfidf_matrix, tfidf_matrix)

# 4.3 FUNCTION TO GET MOVIE-RECOMMENDATIONS BASED ON RATINGS AND SIMILARITY
def get_movie_recommendations(movie_name, rating_threshold=2.0):
    movie_index = movies_df.index[movies_df['MovieName'] == movie_name].tolist()[0]
    
    # Get movies similar to the selected one based on cosine similarity
    similar_movies = list(enumerate(cosine_similarity[movie_index]))
    similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]  # Exclude the movie itself
    
    # Get movies with ratings above the threshold
    high_rated_similar_movies = [(movies_df['MovieName'][i], movie_ratings['Rating'][movie_ratings['MovieID'] == i].mean())
    for i, _ in similar_movies if movie_ratings['Rating'][movie_ratings['MovieID'] == i].mean() > rating_threshold]
    
    # Sort movies based on average ratings
    high_rated_similar_movies = sorted(high_rated_similar_movies, key=lambda x: x[1], reverse=True)
    return high_rated_similar_movies


# 5. TAKE INPUT FROM USER
print("\nSimple Movie Recommendation System")

movie_name = input("\nEnter the Movie Name: ")
recommendations = get_movie_recommendations(movie_name)

print(f"\nTop Movie Recommendations for '{movie_name}' based on User Preferences Using Content-Based Filtering")
for movie, rating in recommendations:
    print(f"{movie} (Average Rating: {rating:.2f})")
