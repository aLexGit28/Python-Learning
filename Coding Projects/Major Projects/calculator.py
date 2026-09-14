# =====================================
# RESIZABLE CALCULATOR USING TKINTER
# =====================================

from tkinter import * # type: ignore
# =====================================
# CREATING MAIN WINDOW
# =====================================

root = Tk()
root.title("Calculator")
root.geometry("400x500")
root.config(bg="lightblue")

# Makes window resizable
root.resizable(True, True)


# =====================================
# FUNCTION TO DISPLAY VALUES
# =====================================

def click(value):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(END, current + str(value))


# =====================================
# FUNCTION TO CLEAR SCREEN
# =====================================

def clear():
    entry.delete(0, END)


# =====================================
# FUNCTION TO CALCULATE RESULT
# =====================================

def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)

    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


# =====================================
# ENTRY BOX
# =====================================

entry = Entry(root,
              font=("Arial", 28),
              bd=5,
              relief=RIDGE,
              justify="right")

entry.grid(row=0,
           column=0,
           columnspan=4,
           padx=10,
           pady=10,
           sticky="nsew",
           ipadx=8,
           ipady=15)


# =====================================
# BUTTON DETAILS
# =====================================

buttons = [
    ('7', 1, 0),
    ('8', 1, 1),
    ('9', 1, 2),
    ('/', 1, 3),

    ('4', 2, 0),
    ('5', 2, 1),
    ('6', 2, 2),
    ('X', 2, 3),

    ('1', 3, 0),
    ('2', 3, 1),
    ('3', 3, 2),
    ('-', 3, 3),

    ('0', 4, 0),
    ('.', 4, 1),
    ('=', 4, 2),
    ('+', 4, 3)
]


# =====================================
# CREATING BUTTONS USING LOOP
# =====================================

for (text, row, column) in buttons:

    # Equal button
    if text == "=":
        Button(root,
               text=text,
               font=("Arial", 20),
               bg="lightgreen",
               command=equal
               ).grid(row=row,
                      column=column,
                      padx=5,
                      pady=5,
                      sticky="nsew")

    # Other buttons
    else:
        Button(root,
               text=text,
               font=("Arial", 20),
               command=lambda value=text: click(value)
               ).grid(row=row,
                      column=column,
                      padx=5,
                      pady=5,
                      sticky="nsew")


# =====================================
# CLEAR BUTTON
# =====================================

Button(root,
       text="CLEAR",
       font=("Arial", 18),
       bg="tomato",
       command=clear
       ).grid(row=5,
              column=0,
              columnspan=4,
              padx=5,
              pady=5,
              sticky="nsew")


# =====================================
# MAKING ROWS AND COLUMNS RESIZABLE
# =====================================

for i in range(6):
    root.grid_rowconfigure(i, weight=1)

for j in range(4):
    root.grid_columnconfigure(j, weight=1)


# =====================================
# RUNNING THE WINDOW
# =====================================
root.mainloop()