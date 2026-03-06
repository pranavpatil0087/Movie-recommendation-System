# 🎬 Movie Recommender System

This is a content-based movie recommendation system built using Python, Streamlit, and Machine Learning.

The system recommends movies similar to the one selected by the user.

## Features
- Recommends 5 similar movies
- Displays movie posters using TMDB API
- Built using cosine similarity

## Files
- app.py → Streamlit web application
- movie_dict.pkl → Movie dataset
- similarity.pkl → Not uploaded due to size (can be generated)

## Run the Project

```bash
pip install streamlit pandas requests scikit-learn
streamlit run app.py
