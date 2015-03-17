__author__ = 'mohammedsafwat'

from video import Video

class Show(Video):
    '''A child class for Show extending the parent Video class'''

    def __init__(self, show_title, show_story_line, show_poster_image, show_trailer_url, show_rating, show_tv_station):
        Video.__init__(self, show_title, show_story_line, show_poster_image, show_trailer_url, show_rating)
        self.tv_station = show_tv_station

