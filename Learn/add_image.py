from tkinter import * # type: ignore

root = Tk()
root.title("Image Example")

image = PhotoImage(file="Learn/the_wallpaper.png")

label = Label(root, image=image)
label.pack()

root.mainloop()