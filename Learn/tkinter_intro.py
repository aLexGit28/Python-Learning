import tkinter as tk

root = tk.Tk() #main window
root.title("My app")
root.geometry('400x500')

# add widgets to see on the screen
lbl = tk.Label(root, text="My window for Display", font=('Arial', 18, 'bold'), fg='red', bg='white').pack()

ent = tk.Entry(root, width = 80)
ent.pack()

btn = tk.Button(root, text="Click me", width=20, height=15, command=root.destroy)
btn.pack(pady=10)

root.mainloop()