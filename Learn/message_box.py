from tkinter import *
from tkinter import messagebox

# Create the main window
root = Tk()
root.title("Username Verification System")
root.geometry("400x250")


# Function to check the username
def check_username():

    username = username_entry.get()

    # Predefined correct username
    correct_username = "Ananya"

    if username == correct_username:
        messagebox.showinfo("Success", "Login Successful!")
    else:
        messagebox.showerror("Error", "Incorrect Username!")


# Heading
title = Label(
    root,
    text="Login System",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)


# Username label
username_label = Label(
    root,
    text="Enter Username:",
    font=("Arial", 12)
)
username_label.pack()


# Username input box
username_entry = Entry(
    root,
    font=("Arial", 12)
)
username_entry.pack(pady=10)


# Check button
check_button = Button(
    root,
    text="Login",
    font=("Arial", 12),
    command=check_username
)
check_button.pack(pady=10)


# Run the window
root.mainloop()