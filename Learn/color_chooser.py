from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Color Box")
root.geometry("700x500")

# Text box
text = Text(root, font=("Times New Roman", 20), width=50, height=10)
text.pack(pady=30)


def choose_color():
    color = colorchooser.askcolor(title="Choose a Color")

    if color[1]:
        text.tag_add("color", "1.0", "end")
        text.tag_config("color", foreground=color[1])


# Color button
Button(root, text="Color", font=("Times New Roman", 16),
       command=choose_color).pack(pady=20)

root.mainloop()