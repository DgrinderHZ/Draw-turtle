import turtle

window = turtle.Screen()
window.bgcolor("gray")

pencil = turtle.Turtle()

# Costumizing section!
pencil.shape("turtle")
pencil.speed(20)

pencil.color("gray")
pencil.goto(-150,0)
pencil.color("red")
pencil.right(90)
pencil.forward(200)
pencil.right(180)
pencil.forward(100)
pencil.right(90)
pencil.forward(100)
pencil.right(90)
pencil.forward(100)
pencil.right(180)
pencil.forward(200)
pencil.right(180)
pencil.forward(100)
pencil.right(90)
pencil.forward(100)
pencil.write("Hassan", True, align="left", font=("Arial",23,"italic"))

pencil.right(180)
pencil.color("gray")
pencil.goto(50,0)
pencil.color("red")
pencil.forward(180)
pencil.right(130)
pencil.forward(260)
pencil.left(140)
pencil.write("   Zekkouri", True, align="left", font=("Arial",28,"italic"))

window.exitonclick()