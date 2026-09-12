from tkinter import *

root = Tk()
root.title("Hello Window")
root.geometry("400x300")

Label(root, text="Enter your name:",
      font=("Arial", 16)).pack(pady=20)

name = Entry(root)
name.pack()

def greet():
    user_name = name.get()
    message.config(text="Hello " + user_name + "!")

Button(root, text="Greet Me",
       command=greet).pack(pady=20)

message = Label(root, text="",
                font=("Arial", 18))
message.pack(pady=10)

root.mainloop()