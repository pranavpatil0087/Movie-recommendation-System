import streamlit as st
import pickle
import pandas as pd
import requests

st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
}
h1, h2, h3, p {
    color: white;
}
</style>
""", unsafe_allow_html=True)

def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=5e0b2460a168cea1a3e5b3ca81dfc5e1&language=en-US'.format(movie_id)
    )
    data = response.json()
    print(data)
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))


st.markdown("<h1 style='text-align:center;'>🎬 Movie Recommender System</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Find movies similar to your favorite one</p>", unsafe_allow_html=True)

selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)


if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(posters[0])
        st.markdown(f"**{names[0]}**")

    with col2:
        st.image(posters[1])
        st.markdown(f"**{names[1]}**")

    with col3:
        st.image(posters[2])
        st.markdown(f"**{names[2]}**")

    with col4:
        st.image(posters[3])
        st.markdown(f"**{names[3]}**")

    with col5:
        st.image(posters[4])
        st.markdown(f"**{names[4]}**")  



