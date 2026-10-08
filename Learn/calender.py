from tkinter import * # type: ignore
import calendar

# Create the window
root = Tk()

root.title("Calendar")
root.geometry("700x500")

root.configure(bg="lightgray")


# Function to show the calendar
def show_calendar():

    # Get the year
    year = int(year_entry.get())

    # Get the month
    month = int(month_entry.get())

    # Get the calendar
    cal = calendar.monthcalendar(year, month)

    # Clear the old calendar
    for widget in calendar_frame.winfo_children():
        widget.destroy()

    # Days of the week
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    # Display the days
    for i in range(7):

        day_label = Label(
            calendar_frame,
            text=days[i],
            font=("Arial", 14),
            width=6,
            bg="lightblue",
            fg="white"
        )

        day_label.grid(
            row=0,
            column=i,
            padx=2,
            pady=2
        )

    # Display the dates
    for row in range(len(cal)):

        for column in range(7):

            day = cal[row][column]

            if day == 0:

                empty_label = Label(
                    calendar_frame,
                    text="",
                    width=6,
                    height=2,
                    bg="lightgray"
                )

                empty_label.grid(
                    row=row + 1,
                    column=column,
                    padx=2,
                    pady=2
                )

            else:

                if day % 2 == 0:
                    color = "lightgreen"
                else:
                    color = "lightyellow"

                date_label = Label(
                    calendar_frame,
                    text=day,
                    font=("Arial", 14),
                    width=6,
                    height=2,
                    bg=color,
                    fg="black"
                )

                date_label.grid(
                    row=row + 1,
                    column=column,
                    padx=2,
                    pady=2
                )


# -------------------------
# Year
# -------------------------

year_label = Label(
    root,
    text="Year:",
    font=("Arial", 14),
    bg="lightgray"
)

year_label.place(
    x=20,
    y=30
)


year_entry = Entry(
    root,
    font=("Arial", 14),
    width=15
)

year_entry.place(
    x=130,
    y=30
)

year_entry.insert(0, "2024")


# -------------------------
# Month
# -------------------------

month_label = Label(
    root,
    text="Month:",
    font=("Arial", 14),
    bg="lightgray"
)

month_label.place(
    x=20,
    y=80
)


month_entry = Entry(
    root,
    font=("Arial", 14),
    width=15
)

month_entry.place(
    x=130,
    y=80
)

month_entry.insert(0, "2")


# -------------------------
# Show Calendar Button
# -------------------------

show_button = Button(
    root,
    text="Show Calendar",
    font=("Arial", 14),
    command=show_calendar
)

show_button.place(
    x=145,
    y=125
)


# -------------------------
# Calendar Frame
# -------------------------

calendar_frame = Frame(
    root,
    bg="lightgray"
)

calendar_frame.place(
    x=10,
    y=190
)


# Start the program
root.mainloop()