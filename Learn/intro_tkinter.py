from tkinter import *

root = Tk() 
name = Label(root, text='Name')
name.pack()
text = Entry(root, width=50)
text.pack()
root.geometry('500x600')
root.title('My Window')

mainloop()