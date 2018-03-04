import turtle

window = turtle.Screen()
window.bgcolor("white")

donatilo = turtle.Turtle()
def draw_triangle(color, size):
	for i in range(0,3):
		donatilo.forward(size)
		donatilo.color(color)
		donatilo.right(120)
	

def draw(color, size):
	#Costumizing section
	donatilo.shape("turtle")
	donatilo.speed(10)
	donatilo.color("green")

	donatilo.fill(True)
	donatilo.left(180)
	draw_triangle(color, size)
	donatilo.fill(False)

	donatilo.forward(size/2)
	donatilo.right(60)
	donatilo.fill(True)
	draw_triangle("white", size/2)
	donatilo.fill(False)


color = "green"
size = 100
for x in  range(0,3):
	for i in range(0,3):
	    draw(color, size)
	    donatilo.left(60)
	    donatilo.forward(size/2)
	    donatilo.right(60)
	if x < 1:
		donatilo.right(60)
		donatilo.forward(size)
		donatilo.right(60)
		donatilo.forward(size)
		donatilo.right(120)
	else:
		donatilo.right(120)
		donatilo.forward(-size)


window.exitonclick()