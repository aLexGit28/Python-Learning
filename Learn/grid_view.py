# import tkinter module
from tkinter import * 
from tkinter.ttk import * # more beautiful widgets

# creating main tkinter window/toplevel
master = Tk()
master.geometry("300x300")
# this will create a label widget
l1 = Label(master, text = "First:")
l2 = Label(master, text = "Second:")

# grid method to arrange labels in respective
# rows and columns as specified
l1.grid(row = 0, column = 0, sticky = W, pady = 3)
l2.grid(row = 1, column = 0, sticky = W, pady = 3)

# entry widgets, used to take entry from user
e1 = Entry(master)
e2 = Entry(master)

# this will arrange entry widgets
e1.grid(row = 0, column = 1, pady = 7)
e2.grid(row = 1, column = 1, pady = 7)

# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()
