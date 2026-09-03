import turtle

t = turtle.Turtle()

t.color("blue")
t.fillcolor("skyblue")

t.begin_fill()
for i in range(4):
    t.forward(100)
    t.left(90)
t.end_fill()

t.penup()
t.goto(150,100)
t.pendown()

t.color("red")
t.dot(30)

turtle.done()
