from tkinter import *

# Create window
root = Tk()
root.title("Weather Simulator")
root.geometry("600x500")

# Create canvas
canvas = Canvas(root, width=600, height=400, bg="skyblue")
canvas.pack()

# Function for sunny weather
def sunny():
    canvas.delete("all")
    canvas.config(bg="skyblue")

    # Sun
    canvas.create_oval(250, 100, 350, 200, fill="yellow")

# Function for rainy weather
def rainy():
    canvas.delete("all")
    canvas.config(bg="gray")

    # Clouds
    canvas.create_oval(180, 100, 300, 160, fill="white")
    canvas.create_oval(250, 80, 380, 160, fill="white")

    # Rain drops
    for x in range(200, 381, 30):
        canvas.create_line(x, 170, x - 10, 220, fill="blue", width=3)

# Function for snowy weather
def snowy():
    canvas.delete("all")
    canvas.config(bg="lightblue")

    # Cloud
    canvas.create_oval(200, 100, 320, 160, fill="white")
    canvas.create_oval(280, 80, 400, 160, fill="white")

    # Snow
    for x in range(200, 401, 40):
        canvas.create_oval(x, 180, x + 10, 190, fill="white")

# Buttons
Button(root, text="Sunny", command=sunny).pack(side=LEFT, padx=50)
Button(root, text="Rainy", command=rainy).pack(side=LEFT, padx=50)
Button(root, text="Snowy", command=snowy).pack(side=LEFT, padx=50)

root.mainloop()