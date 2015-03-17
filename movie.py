__author__ = 'mohammedsafwat'

from video import Video

class Movie(Video):
    '''A child class for Movie extending the parent Video class'''

    def __init__(self, movie_title, movie_story_line, movie_poster_image, movie_trailer_url, movie_rating):
        Video.__init__(self, movie_title, movie_story_line, movie_poster_image, movie_trailer_url, movie_rating)
