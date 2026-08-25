movies = ["Avengers: Endgame", "The Lion King", "Inception"]

price = 12
total_bill = 0

# Create theatre seats
seats = []

for i in range(5):
    row = []

    for j in range(10):
        row.append("-")

    seats.append(row)

while True:

    print("\nAvailable movies:")

    for i in range(len(movies)):
        print(i + 1, ".", movies[i])

    choice = int(input("Enter the number of the movie you want to watch (0 to exit): "))

    if choice == 0:
        print("Thank you for using the Movie Ticket System!")
        break

    tickets = int(input("Enter the number of tickets you want to book: "))

    total_bill = total_bill + (tickets * price)

    print("\nScreen\n")

    # Display seats
    for row in seats:
        for seat in row:
            print(seat, end=" ")
        print()

    # Book seats
    for t in range(tickets):

        row_num = int(input("Enter row number for your seat: ")) - 1
        col_num = int(input("Enter column number for your seat: ")) - 1

        seats[row_num][col_num] = "X"

    print("\nYou've booked", tickets, "ticket(s) for", movies[choice - 1])
    print("Your total bill so far is: $", total_bill)

    print("\nUpdated Seat Layout:\n")

    # Display updated seats
    for row in seats:
        for seat in row:
            print(seat, end=" ")
        print()
