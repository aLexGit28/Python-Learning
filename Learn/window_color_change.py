import tkinter as tk

# Create window
root = tk.Tk()
root.title("Color Changer App")
root.geometry("400x250")

# Function to change background color
def change_color():
    color = entry.get()
    root.config(bg=color)

# Label
label = tk.Label(root, text="Enter a color name:")
label.pack(pady=10)

# Entry
entry = tk.Entry(root)
entry.pack(pady=5)

# Button
button = tk.Button(root, text="Change Color", command=change_color)
button.pack(pady=10)

# Run app
root.mainloop()