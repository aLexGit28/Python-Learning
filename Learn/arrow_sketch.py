import tkinter as tk

root = tk.Tk()
root.title("Arrow Sketch")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack()

x = 300
y = 200

def move(event):
    global x, y

    old_x = x
    old_y = y

    if event.keysym == "Up":
        y -= 10
    elif event.keysym == "Down":
        y += 10
    elif event.keysym == "Left":
        x -= 10
    elif event.keysym == "Right":
        x += 10

    canvas.create_line(old_x, old_y, x, y, width=3)

root.bind("<Up>", move)
root.bind("<Down>", move)
root.bind("<Left>", move)
root.bind("<Right>", move)

root.mainloop()