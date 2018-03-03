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
	pencil = turtle.Turtle()
	# Costumizing section!
	pencil.shape("turtle")
	pencil.color("yellow")
	pencil.speed(10)

	for x in range(0,4):
		pencil.forward(100)
		pencil.right(90)

def draw_circle():
	pen = turtle.Turtle()
	# Costumizing section!
	pen.shape("arrow")
	pen.color("green")
	pen.circle(100)

window = turtle.Screen()
window.bgcolor("red")
draw_square()
draw_circle()
window.exitonclick()