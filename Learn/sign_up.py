from tkinter import * # type: ignore

root = Tk()
root.title("Login")
root.geometry("400x200")

def submit():
    username = username_entry.get()
    password = password_entry.get()

    print("The name is:", username)
    print("The password is:", password)


Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)

username_entry = Entry(root)
username_entry.grid(row=0, column=1)

Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)

password_entry = Entry(root, show="*")
password_entry.grid(row=1, column=1)

Button(root, text="Submit", command=submit).grid(
    row=2, column=1, pady=10
)

root.mainloop()