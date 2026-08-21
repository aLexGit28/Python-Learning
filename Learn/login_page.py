import tkinter as tk
from tkinter import messagebox, ttk


def submit_login() -> None:
    username = username_var.get().strip()
    password = password_var.get()
    confirm_password = confirm_password_var.get()

    if not username or not password or not confirm_password:
        messagebox.showwarning("Missing details", "Please fill in all fields.")
    elif password != confirm_password:
        messagebox.showerror("Password mismatch", "Passwords do not match.")
    else:
        messagebox.showinfo("Login successful", f"Welcome, {username}!")


root = tk.Tk()
root.title("Login Page")
root.geometry("400x300")
root.resizable(True, True)

main_frame = ttk.Frame(root, padding=30)
main_frame.pack(fill="both", expand=True)

ttk.Label(main_frame, text="Login", font=("Arial", 20, "bold")).pack(pady=(0, 20))

username_var = tk.StringVar()
password_var = tk.StringVar()
confirm_password_var = tk.StringVar()

ttk.Label(main_frame, text="Username").pack(anchor="w")
ttk.Entry(main_frame, textvariable=username_var).pack(fill="x", pady=(0, 10))

ttk.Label(main_frame, text="Password").pack(anchor="w")
ttk.Entry(main_frame, textvariable=password_var, show="*").pack(fill="x", pady=(0, 10))

ttk.Label(main_frame, text="Confirm password").pack(anchor="w")
ttk.Entry(main_frame, textvariable=confirm_password_var, show="*").pack(
    fill="x", pady=(0, 20)
)

ttk.Button(main_frame, text="Login", command=submit_login).pack(fill="x")

root.mainloop()
