# Dictionary containing movies and their details
movies = {
    1: {
        "name": "Avengers: Endgame",
        "price": 12,
        "available_seats": 50
    },
    2: {
        "name": "The Lion King",
        "price": 10,
        "available_seats": 50
    },
    3: {
        "name": "Inception",
        "price": 15,
        "available_seats": 50
    },
    4: {
        "name": "Interstellar",
        "price": 14,
        "available_seats": 50
    }
}


# Create seats for each movie
for movie in movies:
    seats = []

    for i in range(5):
        row = []

        for j in range(10):
            row.append("-")

        seats.append(row)

    movies[movie]["seats"] = seats


total_bill = 0


while True:

    print("\n==============================")
    print("       MOVIE TICKET SYSTEM")
    print("==============================")

    print("\nAvailable Movies:")

    for movie_number in movies:
        movie = movies[movie_number]

        print(
            movie_number,
            ".",
            movie["name"],
            "- $", movie["price"],
            "- Available seats:", movie["available_seats"]
        )

    print("0. Exit")

    choice = int(input("\nEnter the number of the movie: "))

    # Exit
    if choice == 0:
        print("\nThank you for using the Movie Ticket System!")
        print("Your final bill is: $", total_bill)
        break

    # Check whether movie exists
    if choice not in movies:
        print("Invalid movie choice!")
        continue

    # Get selected movie
    selected_movie = movies[choice]

    print("\nYou selected:", selected_movie["name"])
    print("Ticket price: $", selected_movie["price"])
    print("Available seats:", selected_movie["available_seats"])


    # Ask how many tickets
    tickets = int(input("\nEnter the number of tickets you want to book: "))


    # Check availability
    if tickets > selected_movie["available_seats"]:
        print(
            "Sorry! Only",
            selected_movie["available_seats"],
            "seat(s) are available."
        )
        continue


    print("\n========== SCREEN ==========")

    # Display seats
    for row in selected_movie["seats"]:

        for seat in row:
            print(seat, end=" ")

        print()


    # Book seats
    booked_count = 0

    while booked_count < tickets:

        print("\nBooking seat", booked_count + 1, "of", tickets)

        row_num = int(input("Enter row number (1-5): "))
        col_num = int(input("Enter column number (1-10): "))


        # Check whether row and column are valid
        if row_num < 1 or row_num > 5:
            print("Invalid row number! Please choose 1-5.")
            continue

        if col_num < 1 or col_num > 10:
            print("Invalid column number! Please choose 1-10.")
            continue


        # Convert to Python index
        row_index = row_num - 1
        col_index = col_num - 1


        # Check whether seat is already booked
        if selected_movie["seats"][row_index][col_index] == "X":

            print(
                "❌ This seat is already booked!",
                "Please choose another seat."
            )

            continue


        # Book the seat
        selected_movie["seats"][row_index][col_index] = "X"

        booked_count += 1

        # Reduce available seats
        selected_movie["available_seats"] -= 1

        print("✅ Seat booked successfully!")


    # Calculate bill
    bill = tickets * selected_movie["price"]

    total_bill += bill


    print("\n==============================")
    print("Booking successful!")
    print("Movie:", selected_movie["name"])
    print("Tickets:", tickets)
    print("Current booking: $", bill)
    print("Total bill: $", total_bill)
    print("Available seats:", selected_movie["available_seats"])
    print("==============================")


    # Display updated seats
    print("\nUpdated Seat Layout:\n")

    for row in selected_movie["seats"]:

        for seat in row:
            print(seat, end=" ")

        print()