# Movie_Recommendation_System
# Movie Recommendation Web App

This Python script creates an interactive web application for movie recommendations using the Streamlit framework. The application allows users to discover movies similar to their favorite titles.

## How It Works

1. **Data Loading:** The script loads movie data from a CSV file, which should contain information about movies, including genres, keywords, taglines, cast, and director.

2. **Feature Vectorization:** To compare movie similarity, it converts the textual data (genres, keywords, taglines, cast, director) into feature vectors using Term Frequency-Inverse Document Frequency (TF-IDF) vectorization.

3. **Cosine Similarity:** Using the feature vectors, it calculates the cosine similarity between movies, which measures how alike two movies are based on their textual data.

4. **Web App Interface:** The script builds a user-friendly web interface using Streamlit, where users can input their favorite movie's name.

5. **Recommendation:** When users enter a movie name and click "Recommend," the script finds the closest match to the provided title. It then uses the similarity scores to recommend other movies that are similar to the user's favorite.

6. **Results Display:** The recommended movies are displayed in descending order of similarity, providing users with suggestions for their next movie night.

**Background Image:**

The web app features a visually appealing background image to enhance the user experience.

**Please Note:**

- Ensure that you have the necessary movie data in CSV format and specify the file path in the script for it to work correctly.
- You can tailor the recommendation process to your specific dataset and preferences, as the current code is a sample implementation.

With this Movie Recommendation Web App, users can easily discover new films that align with their cinematic tastes. Whether you're a movie enthusiast or just looking for something new to watch, this app provides personalized movie recommendations at your fingertips.
