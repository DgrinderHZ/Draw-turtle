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
	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)
	pencil.forward(100)
	pencil.right(90)

	window.exitonclick()

draw_square()