# Mini-Project: Draw Turtles

'''Let's draw a square!
Steps!
 move forward - turn right
 move forward - turn right
 move forward - turn right
 move forward - turn right
'''
import turtle

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	pencil = turtle.Turtle()
	# Costumizing section!
	pencil.shape("turtle")
	pencil.color("yellow")
	pencil.speed(10)

	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)

	pen = turtle.Turtle()
	pen.shape("arrow")
	pen.color("green")
	pen.circle(100)

	window.exitonclick()

draw_square()