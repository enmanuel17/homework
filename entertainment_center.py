#enmaneul hernandez
#movie trailer website
#part of code are from udacity learning material

import media
import fresh_tomatoes

#creates a toy story movie object
toy_story = media.Movie("Toy Story","Story of a boy and his toys that come to life","http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg","http://www.youtube.com/watch?v=vwyZH85NQC4")

#creates an avatar movie object
avatar = media.Movie("Avatar","A marine on an alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","http://www.youtube.com/watch?v=-9ceBgWV8io")

#create the 300 spatants movei object(my favorite movei)
the300spartants = media.Movie("300","King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 B.C.","https://upload.wikimedia.org/wikipedia/en/5/5c/300poster.jpg","https://www.youtube.com/watch?v=ZJ6yq-oVKPc")

#print(toy_story.storyline)
#avatar.show_trailer()
#print(the300spartants.storyline)
#the300spartants.show_trailer()

#creates an array that holds the name of each movie object
movies = [toy_story, avatar, the300spartants]
fresh_tomatoes.open_movies_page(movies)
