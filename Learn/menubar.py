import tkinter as tk


def new_file():
    pass


def open_file():
    pass


def save_file():
    pass


# Creating tkinter window
root = tk.Tk()

root.title('Menu Demonstration')


# Creating Menubar
menubar = tk.Menu(root)


# Creating File Menu
file = tk.Menu(
    menubar,
    tearoff=0
)


# Adding File Menu
menubar.add_cascade(
    label='File',
    menu=file
)


# Adding commands
file.add_command(
    label='New File',
    command=new_file
)

file.add_command(
    label='Open...',
    command=open_file
)

file.add_command(
    label='Save',
    command=save_file
)


# Separator
file.add_separator()


# Exit command
file.add_command(
    label='Exit',
    command=root.destroy
)


# Display menu
root.config(menu=menubar)


root.mainloop()