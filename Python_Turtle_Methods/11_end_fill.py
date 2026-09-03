import turtle

t = turtle.Turtle()

t.fillcolor("green")
t.begin_fill()

for i in range(4):
    t.forward(80)
    t.left(90)

t.end_fill()

turtle.done()
