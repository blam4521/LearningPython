import webbrowser

class Movie():
	"""writes out movie information"""
	def __init__( self, movie_title, movie_storyline, poster_image, trailer_youtube):
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube

	def show_trailer( self ):
		webbrowser.open( self.trailer_youtube_url )



batman = Movie("Batman", 
	"A boy loses his parents and becomes a symbol of justice", 
	"http://cdn1-www.superherohype.com/assets/uploads/gallery/batman-vs-superman/12365933_972834219457672_494602726406190890_o.jpg",
	"https://www.youtube.com/watch?v=eX_iASz1Si8")

print(batman.storyline)

batman.show_trailer()


