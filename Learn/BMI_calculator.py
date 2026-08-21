import tkinter as tk


# Function to calculate BMI
def calculate_bmi():

    height = height_slider.get()
    weight = weight_slider.get()

    bmi = weight / (height ** 2)

    bmi_value.config(text=f"{bmi:.2f}")


# Create main window
root = tk.Tk()

root.title("BMI Manager")
root.geometry("600x500")


# Heading
title = tk.Label(
    root,
    text="BMI Calculator",
    font=("Arial", 24, "bold")
)

title.pack(pady=20)


# ---------------- HEIGHT ----------------

height_label = tk.Label(
    root,
    text="Select Height in meters",
    font=("Arial", 16)
)

height_label.pack()


height_value = tk.Label(
    root,
    text="1.35",
    font=("Arial", 18)
)

height_value.pack()


# Function to update height display
def update_height(value):

    height_value.config(
        text=f"{float(value):.2f}"
    )

    calculate_bmi()


height_slider = tk.Scale(
    root,
    from_=1.0,
    to=2.5,
    resolution=0.01,
    orient="horizontal",
    length=500,
    command=update_height
)

height_slider.set(1.35)

height_slider.pack(pady=10)


# ---------------- WEIGHT ----------------

weight_label = tk.Label(
    root,
    text="Select Weight in KGs",
    font=("Arial", 16)
)

weight_label.pack()


weight_value = tk.Label(
    root,
    text="148",
    font=("Arial", 18)
)

weight_value.pack()


# Function to update weight display
def update_weight(value):

    weight_value.config(
        text=f"{float(value):.0f}"
    )

    calculate_bmi()


weight_slider = tk.Scale(
    root,
    from_=30,
    to=200,
    orient="horizontal",
    length=500,
    command=update_weight
)

weight_slider.set(148)

weight_slider.pack(pady=10)


# ---------------- BMI ----------------

bmi_label = tk.Label(
    root,
    text="Your BMI",
    font=("Arial", 16)
)

bmi_label.pack(pady=(20, 0))


bmi_value = tk.Label(
    root,
    text="",
    font=("Arial", 22, "bold")
)

bmi_value.pack()


# ---------------- BUTTON ----------------

result_button = tk.Button(
    root,
    text="Your BMI Result",
    font=("Arial", 16),
    command=calculate_bmi
)

result_button.pack(pady=20)


# Calculate initial BMI
calculate_bmi()


# Run application
root.mainloop()