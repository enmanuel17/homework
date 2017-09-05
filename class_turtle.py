#enmanuel hernandez
#program to midstorm with classes in python

import turtle

def draw_square():
	window = turtle.Screen() #sets the screen for the turtle
	window.bgcolor("red") #sets the color of the screen
	
	#creates a turtle object name brad.
	brad = turtle.Turtle()

	#changes the color of the turtle
	brad.color("blue")
	#changes the shape of the turtle
	brad.shape("turtle")
	#changes the speed of the turtle
	brad.speed(5)
	#creates a square
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)
	brad.forward(100)
	brad.right(90)

	#class a function that allow the progem to close upon click.
	window.exitonclick()

draw_square()