from tkinter import *

root = Tk()
root.title("Drag Box")
root.geometry("500x400")

canvas = Canvas(root, width=500, height=400)
canvas.pack()

# Create blue box
box = canvas.create_rectangle(200, 150, 300, 250, fill="blue")

# Start dragging
def start_drag(event):
    global old_x, old_y
    old_x = event.x
    old_y = event.y

# Move the box
def drag(event):
    global old_x, old_y

    dx = event.x - old_x
    dy = event.y - old_y

    canvas.move(box, dx, dy)

    old_x = event.x
    old_y = event.y

# Mouse events
canvas.bind("<Button-1>", start_drag)
canvas.bind("<B1-Motion>", drag)

root.mainloop()