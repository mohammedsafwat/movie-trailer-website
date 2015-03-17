__author__ = 'mohammedsafwat'
import webbrowser

class Video():
    '''A parent class for any type of videos, either movies, tv shows, etc.'''

    #init method
    def __init__(self, video_title, video_story_line, video_poster_image, video_trailer_url, video_rating):
        self.title = video_title
        self.story_line = video_story_line
        self.poster_image_url = video_poster_image
        self.trailer_youtube_url = video_trailer_url
        self.rating = video_rating

    #A method used to open youtube trailer for the video
    #@param self.trailer_link the link for youtube trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_link)

