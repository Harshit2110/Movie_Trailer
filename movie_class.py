#import webbrowser 

class Movie():
    def __init__(self,movie_title,movie_storyline,poster_image,trailer_youtube,lead_1,lead_2,lead_3,director):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.lead_1 = lead_1
        self.lead_2 = lead_2
        self.lead_3 = lead_3
        self.director = director

   # def show_trailer(self):
    #    webbrowser.open(self.trailer_youtube_url)
