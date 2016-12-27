""" This file is use to generate a html for the movies """

import webbrowser
import os
import re

# Styles and scripting for the page
MAIN_PAGE_HEAD = '''
<!DOCTYPE html>
<html>

<head>
  <link rel="stylesheet" type="text/css" href="css/styles.css">
  <!-- Compiled and minified CSS -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/css/materialize.min.css">
  <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>

  <!-- Compiled and minified JavaScript -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/0.97.8/js/materialize.min.js"></script>

</head>
'''
#here we are adding main body of the html
MAIN_PAGE_CONTENT = '''
<body>

  <!-- Modal Structure -->
  <div id="trailer" class="modal black">
    <div class="modal-content">
      <div class="modal-dialog">
        <div class="scale-media" id="trailer-video-container">
        </div>
      </div>
    </div>
  </div>
  <div class="container">
    <nav>
      <div class="nav-wrapper grey darken-2">
        <a href="#" class="brand-logo center">My Favourite Movies</a>
      </div>
    </nav>
    <div class="well">
    {movie_tiles}
    </div>
  </div>
<script src="js/script.js" ></script>
</body>

</html>'''

# A single movie entry html template
MOVIE_TILE_CONTENT = '''
  <div class="card modal-trigger"  style="margin-right: 20px" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
      <div class="card-image">
        <img src="{poster_image_url}" height="342px" width="220px" >
      </div>
      <div class="card-content">
        <span class="card-title">{movie_title}</span>
      </div>
    </div>  

        
'''


def create_movie_tiles_content(movies):
    """ The HTML content for this section of the page """
    content = ''

    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += MOVIE_TILE_CONTENT.format(
            movie_title=movie.title,
            storyline=movie.storyline,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    """ Create or overwrite the output file """
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = MAIN_PAGE_CONTENT.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(MAIN_PAGE_HEAD + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
