from tkinter import *

# Create window
root = Tk()
root.title("Simple Drawing Tool")
root.geometry("600x500")

# Function to draw
def draw(event):
    canvas.create_oval(
        event.x - 2,
        event.y - 2,
        event.x + 2,
        event.y + 2,
        fill="black",
        outline="black"
    )

# Create canvas
canvas = Canvas(root, bg="white", width=600, height=450)
canvas.pack()

# Connect mouse movement with drawing
canvas.bind("<B1-Motion>", draw)

# Clear button
def clear():
    canvas.delete("all")

Button(root, text="Clear", command=clear).pack(pady=5)

# Run the program
root.mainloop()