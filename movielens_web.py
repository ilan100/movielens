from unittest import result

import movielens
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

ML = movielens.MovieLens()

# --- Internal function ---
def calculate_number(movies_data: movielens.MovieLens, movie_title: str) -> float:
    if (movies_data.init is False):
        movies_data.load_and_prepare_data()

    average_rating = movies_data.get_movie_average_rating(movie_title)
    return average_rating

# --- OMDB related
OMDB_API_KEY = "4747a790"

def get_omdb_movie_data(title: str):
    url = "http://www.omdbapi.com/"
    params = {
        "t": title,
        "apikey": OMDB_API_KEY
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None

    data = response.json()
    if data.get("Response") == "False":
        return None
    return data

def show_movie_list(movies_data: movielens.MovieLens):
    pass

# --- Routes ---
@app.route("/", methods=["GET", "POST"])
def home():
    result = -1
    movie_title = ""
    #ML = movielens.MovieLens()
    action = request.form.get("action")
    omdb_data = None

    if request.method == "POST":
        if action == "calculate":
            movie_title = request.form.get("movie_title")
            result = calculate_number(ML, movie_title)
        elif action == "fetch":
            if (ML.init is False):
                ML.load_and_prepare_data()

        omdb_data = None
        if result > -1:
            omdb_data = get_omdb_movie_data(movie_title)

    return render_template("index.html", result=result,
                           movie_title=movie_title, action=action, movie=omdb_data, movies = ML.movies)

#-------------------------------------------------------------------------------------------------------

# Run app
if __name__ == "__main__":
    #print("in main......")
    app.run()