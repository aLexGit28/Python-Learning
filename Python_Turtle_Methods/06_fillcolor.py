import turtle

t = turtle.Turtle()

t.fillcolor("blue")
t.begin_fill()

for i in range(4):
    t.forward(100)
    t.right(90)

t.end_fill()

turtle.done()
