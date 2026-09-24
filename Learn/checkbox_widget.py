from tkinter import *

root = Tk()
root.title("Checkbutton Demo")
root.geometry("300x250")

Label(root, text="Select your hobbies").pack()

reading = IntVar()
music = IntVar()
sports = IntVar()

Checkbutton(root, text="Reading", variable=reading).pack()
Checkbutton(root, text="Music", variable=music).pack()
Checkbutton(root, text="Sports", variable=sports).pack()


def show_selection():

    hobbies = ""

    if reading.get() == 1:
        hobbies = hobbies + "Reading "

    if music.get() == 1:
        hobbies = hobbies + "Music "

    if sports.get() == 1:
        hobbies = hobbies + "Sports "

    result.config(text="Selected: " + hobbies)


Button(root, text="Submit", command=show_selection).pack(pady=10)

result = Label(root, text="")
result.pack()

root.mainloop()