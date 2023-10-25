# Load the movies data
#movies_data = pd.read_csv(r'C:\Users\Administrator\Downloads\movies.csv')
import streamlit as st
import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os


# Load the movies data
movies_data = pd.read_csv(r'movies.csv')

# Convert the text data to feature vectors
vectorizer = TfidfVectorizer()
combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']
combined_features = combined_features.fillna("")  # Fill NaN values with empty string
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)


# Streamlit app
def main():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1489599849927-2ee91cede3ba");
    background-size: cover;
    }
    </style>
    """
    st.title("Movie Recommendation App")
    st.write("Enter your favorite movie name:")
    movie_name = st.text_input("Movie Name", "")

    if st.button('Recommend'):
        if movie_name:
            list_of_all_titles = movies_data['title'].tolist()
            find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
            
            if find_close_match:
                close_match = find_close_match[0]
                index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
                
                similarity_score = list(enumerate(similarity[index_of_the_movie]))
                sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)
                
                st.write("Movies suggested for you:")
                i = 1
                for movie in sorted_similar_movies:
                    index = movie[0]
                    title_from_index = movies_data[movies_data.index == index]['title'].values[0]
                    if i < 30:
                        st.write(f"{i}. {title_from_index}")
                        i += 1
            else:
                st.write("No close match found for the provided movie name.")

if __name__ == "__main__":
    main()
