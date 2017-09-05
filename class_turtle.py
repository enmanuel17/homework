#enmanuel hernandez
#program to midstorm with classes in python

import turtle

window = turtle.Screen() #sets the screen for the turtle
window.bgcolor("red") #sets the color of the screen

#Function that creates a circle square with turtle.
def draw_square():
	#creates a turtle object name brad.
	brad = turtle.Turtle()
	#changes the color of the turtle
	brad.color("blue")
	#changes the shape of the turtle
	brad.shape("turtle")
	#changes the speed of the turtle
	brad.speed(5)

	#creates a square by repeating loop until it complete the 4 sides of the square.
	sides = 0
	while (sides < 4):
		brad.forward(100)
		brad.right(90)
		sides = sides + 1 #counter to make the while loop end.
	
#Function that creates a circle object with turtle.
def draw_circle():
	angie = turtle.Turtle()
	angie.shape("arrow")
	angie.color("blue")
	angie.circle(100)

#Function that creates a triangle object with turtle.
def draw_triangle():
	victor = turtle.Turtle()
	victor.shape("triangle")
	victor.color("green")
	
	#creates a trianble by repeating a loop until it complete the 3 sides of a triangle.
	sides = 0
	while (sides < 3):
		victor.forward(100) # go forward 100
		victor.left(120) #move to the left 120 degrees.
		sides = sides + 1 #counter to exit the while loop.
		
#Calls each function to create each object.
draw_square()
draw_circle()
draw_triangle()

#class a function that allow the progem to close upon click.
window.exitonclick()