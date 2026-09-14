from tkinter import * # type: ignore
import random
import time

root = Tk()
root.geometry("1200x700+0+0")
root.title("Restaurant Management System")

# Frames
Tops = Frame(root, bg="white", width=1200, height=50, relief=SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root, width=1100, height=700, relief=SUNKEN)
f1.pack(side=LEFT)

# TIME
localtime = time.asctime(time.localtime(time.time()))

# TOP INFORMATION
lblinfo = Label(
    Tops,
    font=("aria", 30, "bold"),
    text="Restaurant Management System",
    fg="steel blue",
    bd=10,
    anchor="w"
)
lblinfo.grid(row=0, column=0)

lbltime = Label(
    Tops,
    font=("aria", 20),
    text=localtime,
    fg="steel blue",
    anchor="w"
)
lbltime.grid(row=1, column=0)


# Variables
rand = StringVar()
Fries = StringVar()
Largefries = StringVar()
Burger = StringVar()
Filet = StringVar()
Drinks = StringVar()
Tax = StringVar()
cost = StringVar()
Total = StringVar()
Cheese_burger = StringVar()


# TOTAL FUNCTION
def Ref():

    x = random.randint(12980, 50876)
    rand.set(str(x))

    cof = float(Fries.get() or 0)
    colfries = float(Largefries.get() or 0)
    cob = float(Burger.get() or 0)
    cofi = float(Filet.get() or 0)
    cochee = float(Cheese_burger.get() or 0)
    codr = float(Drinks.get() or 0)

    costoffries = cof * 25
    costoflargefries = colfries * 40
    costofburger = cob * 35
    costoffilet = cofi * 50
    costofcheeseburger = cochee * 30
    costofdrinks = codr * 35

    subtotal = (
        costoffries +
        costoflargefries +
        costofburger +
        costoffilet +
        costofcheeseburger +
        costofdrinks
    )

    PayTax = subtotal * 0.33
    overall = subtotal + PayTax

    cost.set("Rs. %.2f" % subtotal)
    Tax.set("Rs. %.2f" % PayTax)
    Total.set("Rs. %.2f" % overall)


# RESET FUNCTION
def reset():

    rand.set("")
    Fries.set("")
    Largefries.set("")
    Burger.set("")
    Filet.set("")
    Drinks.set("")
    Tax.set("")
    cost.set("")
    Total.set("")
    Cheese_burger.set("")


# EXIT FUNCTION
def qexit():
    root.destroy()


# PRICE LIST
def price():

    roo = Toplevel(root)
    roo.geometry("600x300+0+0")
    roo.title("Price List")

    Label(
        roo,
        font=("aria", 15, "bold"),
        text="ITEM",
        fg="black"
    ).grid(row=0, column=0)

    Label(
        roo,
        font=("aria", 15, "bold"),
        text="PRICE",
        fg="black"
    ).grid(row=0, column=3)

    items = [
        ("Fries Meal", 25),
        ("Lunch Meal", 40),
        ("Burger Meal", 35),
        ("Pizza Meal", 50),
        ("Cheese Burger", 30),
        ("Drinks", 35)
    ]

    row = 1

    for item, amount in items:

        Label(
            roo,
            font=("aria", 15, "bold"),
            text=item,
            fg="steel blue"
        ).grid(row=row, column=0)

        Label(
            roo,
            font=("aria", 15, "bold"),
            text=amount,
            fg="steel blue"
        ).grid(row=row, column=3)

        row += 1


# ---------------- ORDER DETAILS ----------------

Label(
    f1,
    font=("aria", 16, "bold"),
    text="Order No.",
    fg="steel blue",
    bd=10
).grid(row=0, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=rand,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=0, column=1)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Fries Meal",
    fg="steel blue",
    bd=10
).grid(row=1, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Fries,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=1, column=1)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Lunch Meal",
    fg="steel blue",
    bd=10
).grid(row=2, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Largefries,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=2, column=1)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Burger Meal",
    fg="steel blue",
    bd=10
).grid(row=3, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Burger,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=3, column=1)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Pizza Meal",
    fg="steel blue",
    bd=10
).grid(row=4, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Filet,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=4, column=1)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Cheese Burger",
    fg="steel blue",
    bd=10
).grid(row=5, column=0)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Cheese_burger,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=5, column=1)


# ---------------- BILL DETAILS ----------------

Label(
    f1,
    font=("aria", 16, "bold"),
    text="Drinks",
    fg="steel blue",
    bd=10
).grid(row=0, column=2)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Drinks,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=0, column=3)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Cost",
    fg="steel blue",
    bd=10
).grid(row=1, column=2)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=cost,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=1, column=3)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Tax",
    fg="steel blue",
    bd=10
).grid(row=3, column=2)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Tax,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=3, column=3)


Label(
    f1,
    font=("aria", 16, "bold"),
    text="Total",
    fg="steel blue",
    bd=10
).grid(row=5, column=2)

Entry(
    f1,
    font=("ariel", 16, "bold"),
    textvariable=Total,
    bd=6,
    bg="powder blue",
    justify="right"
).grid(row=5, column=3)


# ---------------- BUTTONS ----------------

Button(
    f1,
    padx=16,
    pady=8,
    bd=10,
    font=("ariel", 16, "bold"),
    width=10,
    text="PRICE",
    bg="green",
    command=price
).grid(row=7, column=0)


Button(
    f1,
    padx=16,
    pady=8,
    bd=10,
    font=("ariel", 16, "bold"),
    width=10,
    text="TOTAL",
    bg="blue",
    command=Ref
).grid(row=7, column=1)


Button(
    f1,
    padx=16,
    pady=8,
    bd=10,
    font=("ariel", 16, "bold"),
    width=10,
    text="RESET",
    bg="yellow",
    command=reset
).grid(row=7, column=2)


Button(
    f1,
    padx=16,
    pady=8,
    bd=10,
    font=("ariel", 16, "bold"),
    width=10,
    text="EXIT",
    bg="red",
    command=qexit
).grid(row=7, column=3)


root.mainloop()