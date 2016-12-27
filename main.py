
import json
import generate_html
from movie import Movie

with open('movies.json') as data_file:
    MOVIES = json.load(data_file)["movies"]

MOVIES_ARRAY = []

""" Here we will be looping
 through all the movies in movies.json file
 and making a Movie object of each """
 
for MOVIE in MOVIES:
    movie = Movie(MOVIE['title'], 'storyline',
                  MOVIE['poster_image_url'], MOVIE['trailer_youtube_url'])
    MOVIES_ARRAY.append(movie)

generate_html.open_movies_page(MOVIES_ARRAY)
