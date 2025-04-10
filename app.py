import pickle
import streamlit as st
import requests
import pandas as pd
import webbrowser

# REMOVING UNWANTED THINGS
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)



def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_review = []
    for i in distances[1:6]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_review.append(movies.iloc[i[0]].review)

    return recommended_movie_names,recommended_movie_posters,recommended_movie_review


st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="margin-bottom: 5px;">MOVIES RECOMMENDER AND REVIEW</h2>
    <hr style="border: none; height: 2px; background-color: gray; width: 100%;">
</div>
""", unsafe_allow_html=True)
movies = pickle.load(open('artifacts/movie_list.pkl','rb'))
similarity = pickle.load(open('artifacts/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("Type or select a movie from the dropdown", movie_list)


if st.button('Show Recommendation'):
    recommended_movie_names,recommended_movie_posters,recommended_movie_review = recommend(selected_movie)


    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
        st.text(f" --- RATING  =  {recommended_movie_review[0]} ---")

    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
        st.text(f" --- RATING  =  {recommended_movie_review[1]} ---")

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
        st.text(f" --- RATING  =  {recommended_movie_review[2]} ---")

    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
        st.text(f" --- RATING  =  {recommended_movie_review[3]} ---")
        
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
        st.text(f" --- RATING  =  {recommended_movie_review[4]} ---")
        



st.header('You can also Rate any Movies')

google_form_link = "https://forms.gle/sPwZS54CnmjPM9mZA"

st.link_button("REVIEW", google_form_link)



st.header('You can also Rate the Latest Movies')

google_form_link = "https://forms.gle/AdYdH7C9D7iGkeSR6"

st.link_button("REVIEW", google_form_link)


#UPDATING

st.markdown("""
<div style="text-align: center; margin-bottom: 20px;">
    <h2 style="margin-bottom: 5px;">THE LATEST MOVIES</h2>
    <hr style="border: none; height: 2px; background-color: gray; width: 100%;">
</div>
""", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid gray; width: 80%; margin: auto;'>", unsafe_allow_html=True)

### MOVIE 1 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 5.81
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.99
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/01.jpg", caption="VIDAAMUYARCHI", width=300)


### MOVIE 2 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 7.25
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/02.webp", caption="KUDUMBASTHAN", width=300)

### MOVIE 3 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 8.61
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/03.jpg", caption="DRAGON", width=300)


### MOVIE 4 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 6.37
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/04.jpg", caption="KADHALIKKA NERAMILLAI", width=300)


### MOVIE 5 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 6.68
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/05.jpg", caption="CAPTAIN AMERICA: BRAVE NEW WORLD", width=300)


### MOVIE 6 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 6.49
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/06.jpg", caption="MADHA GAJA RAJA", width=300)


### MOVIE 7 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 5.58
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/07.jpg", caption="GAME CHANGER", width=300)

### MOVIE 8 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 7.09
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/08.jpg", caption="SORGAVAASAL", width=300)


### MOVIE 9 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 8.03
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/09.jpg", caption="VIDUTHALAI: PART II", width=300)


### MOVIE 10 ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Rating details
review_score = 5.72
full_stars = int(review_score)
half_star = (review_score - full_stars) >= 0.25 and (review_score - full_stars) < 0.75
empty_stars = 10 - full_stars - (1 if half_star else 0)

# Star display
stars = "★" * full_stars + "⯪" * half_star + "☆" * empty_stars

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 3])  # adjust width ratio if needed

with col3:
    
    st.markdown("<div style='font-size: 20px;'>     </div>", unsafe_allow_html=True)
    st.write("Rating of 65 Peoples")
    st.markdown(f"<div style='font-size: 26px; color: gold;'>{stars}</div>", unsafe_allow_html=True)
    st.write(f"{review_score}/10")

with col1:
    st.image("data/10.jpg", caption="KANGUVA", width=300)


