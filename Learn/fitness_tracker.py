from tkinter import *

root = Tk()
root.title("Fitness Tracker")
root.geometry("500x600")

Label(root, text="Fitness Tracker",
      font=("Arial", 28, "bold")).pack(pady=20)

Label(root, text="Enter Steps:",
      font=("Arial", 16)).pack()

steps = Entry(root)
steps.pack(pady=10)

Label(root, text="Enter Calories Burned:",
      font=("Arial", 16)).pack()

calories = Entry(root)
calories.pack(pady=10)

Label(root, text="Select Activity:",
      font=("Arial", 16)).pack()

activity = StringVar()
activity.set("Walking")

OptionMenu(root, activity, "Walking", "Running", "Cycling", "Swimming").pack()

def log_activity():
    print("Steps:", steps.get())
    print("Calories:", calories.get())
    print("Activity:", activity.get())

def show_summary():
    print("\nDaily Summary")
    print("Steps:", steps.get())
    print("Calories:", calories.get())
    print("Activity:", activity.get())

Button(root, text="Log Activity",
       command=log_activity,
       font=("Arial", 14)).pack(pady=20)

Button(root, text="Show Daily Summary",
       command=show_summary,
       font=("Arial", 14)).pack(pady=20)

root.mainloop()