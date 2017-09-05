#enmanuel hernandez
#profanity checker that checks a file for bad words in it.
#parts of the code are from udacity learning course.


import urllib

#defines a function to read the contents of a file and check for bad words.
def read_text():
	quotes = open(r"/home/enmanuel/homework/homework/movie_quotes.txt") #uses a file descriptor to open a file.
	#reads the contents of file from the object quotes.
	file_contents = quotes.read()
	print(file_contents) #print the contents of the file to the screen.
	quotes.close() #it is a good practice to close the file.
	check_profanity(file_contents)

def check_profanity(text_to_check):
	#creates an object with a connection the the website that check the bad words.
	connection = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text_to_check)
	#reads the out of the profany check.
	output = connection.read()
	#prints the output to the screen
	#print(output)
	connection.close() #closes the connection to the website.
	if "true" in output:
		print("Bad word detected!!")
	elif "false" in output:
		print("This file does not contain bad words :D")
	else:
		print("Could not scan the file properly")

read_text()

