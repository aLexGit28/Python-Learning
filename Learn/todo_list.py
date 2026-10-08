from tkinter import * # type: ignore

# Create the window
root = Tk()
root.title("To-Do List Manager")
root.geometry("800x500")
root.configure(bg="#333333")


# Function to add a task
def add_task():

    task = task_entry.get()

    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)


# Task label
task_label = Label(
    root,
    text="Task:",
    font=("Arial", 20),
    bg="#333333",
    fg="white"
)
task_label.place(x=150, y=50)


# Entry box
task_entry = Entry(
    root,
    font=("Arial", 18),
    width=40
)
task_entry.place(x=250, y=45)


# Add Task button
add_button = Button(
    root,
    text="Add Task",
    font=("Arial", 18),
    bg="#2196F3",
    fg="white",
    width=20,
    command=add_task
)
add_button.place(x=50, y=120)


# Your Tasks label
tasks_label = Label(
    root,
    text="Your Tasks:",
    font=("Arial", 20),
    bg="#333333",
    fg="white"
)
tasks_label.place(x=50, y=190)


# Listbox
task_list = Listbox(
    root,
    font=("Arial", 18),
    width=50,
    height=10,
    bg="#333333",
    fg="white",
    borderwidth=0
)
task_list.place(x=50, y=230)


# Start the program
root.mainloop()