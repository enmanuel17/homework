#enmanuel hernandez
#profanity checker that checks a file for bad words in it.
#parts of the code are from udacity learning course.

#defines a function to read the contents of a file and check for bad words.
def read_text():
	quotes = open(r"/home/enmanuel/homework/homework/") #uses a file descriptor to open a file.
	#reads the contents of file from the object quotes.
	file_contents = quotes.read()
	print(file_contents) #print the contents of the file to the screen.
	quotes.close() #it is a good practice to close the file.

read_text()
