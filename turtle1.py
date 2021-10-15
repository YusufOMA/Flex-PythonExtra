import turtle

turtle.speed(0)
turtle.bgcolor("black")
turtle.pencolor("red")
turtle.fillcolor("white")
turtle.begin_fill()

for x in range(10):
    turtle.forward(50)
    turtle.right(70)
    turtle.forward(50)
    turtle.right(60)
    turtle.forward(110)
    turtle.right(80)
    turtle.forward(150)
    turtle.left(100)

turtle.end_fill()
turtle.done()