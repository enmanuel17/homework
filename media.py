#enmaneul hernandez
#movie trailer website
#part of code are from udacity learning material

import webbrowser
#class that make the blueprint for movie objects
class Movie():
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
	
	#opens a web browser with the trailer of the movie
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)
	
