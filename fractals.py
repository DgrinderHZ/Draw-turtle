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

	donatilo.forward(100)
	donatilo.right(60)
	donatilo.fill(True)
	draw_triangle("white", size/2)
	donatilo.fill(False)


color = "green"
size = 200
for i in range(0,3):
	draw(color, size)
	donatilo.left(60)
	donatilo.forward(100)
	donatilo.right(180)
	donatilo.left(120)

window.exitonclick()