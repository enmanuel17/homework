#Enmauel Hernandez
#program that helps user take break for a predefine amount of time.
#part of code were taken from the udacity learning videos.

import webbrowser
import time

numBreaks = 3   #variable that holds the amount of break we need to take
breaksTaken = 0 #counter variable that holds the breaks we took
timer = 5 #time for each break

#Prints a statement to the terminal to indicate the program has been started and the time in the system.
print ("Starting program "+time.ctime())

#while loop that runs untill the amount of breaks is taken.
while ( breaksTaken < numBreaks):
	time.sleep(timer) #timer to trigger each break
	print "taking a break now"
	webbrowser.open("https://www.youtube.com/watch?v=ZJ6yq-oVKPc") #calls the fuction web browser to open a video on a computers browser.
	breaksTaken = breaksTaken + 1 #counter that helps the while loop end.




