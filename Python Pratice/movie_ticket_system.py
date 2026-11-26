movies = ["Avengers: Endgame", "The Lion King", "Inception"]
ticket_price = 12
total_bill = 0

# Create a 5x10 seating grid for each movie using standard loops
seats = {}
for movie_num in range(1, 4):
    grid = []
    for row_idx in range(5):
        row = []
        for col_idx in range(10):
            row.append("_")
        grid.append(row)
    seats[movie_num] = grid

while True:
    print("Available movies:")
    for i in range(len(movies)):
        print(f"{i + 1}. {movies[i]}")

    choice = int(input("Enter the number of the movie you want to watch (0 to exit): "))

    if choice == 0:
        break

    if choice not in seats:
        print("Invalid movie choice. Please try again.")
        continue

    num_tickets = int(input("Enter the number of tickets you want to book: "))

    # Display the current theatre seating pattern using nested loops
    print("Screen")
    for row in seats[choice]:
        for seat in row:
            print(seat, end=" ")
        print()

    # Calculate and update total bill
    total_bill += num_tickets * ticket_price
    print(f"You've booked {num_tickets} ticket(s) for {movies[choice - 1]}.")
    print(f"Your total bill so far is: ${total_bill}")

    # Let the user choose seats and mark them as 'X'
    for ticket in range(num_tickets):
        while True:
            r = int(input("Enter row number for your seat: ")) - 1
            c = int(input("Enter column number for your seat: ")) - 1

            if 0 <= r < 5 and 0 <= c < 10:
                if seats[choice][r][c] == "_":
                    seats[choice][r][c] = "X"
                    break
                else:
                    print("Seat already booked! Choose another seat.")
            else:
                print("Invalid seat position! Row must be 1-5 and Column 1-10.")

print(f"\nThank you for booking! Your final total bill is: ${total_bill}")
