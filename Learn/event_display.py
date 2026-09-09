from tkinter import *

root = Tk()
root.title("Event Display")
root.geometry("400x300")

label = Label(root, text="Press any key", font=("Arial", 20))
label.pack(pady=100)

def key_pressed(event):
    label.config(text="You pressed: " + event.keysym)

root.bind("<Key>", key_pressed)

root.mainloop()