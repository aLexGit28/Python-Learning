# Empty dictionary to store item names and prices
cart = {}


# Function to add an item
def add_item():
    item_name = input("Enter item name: ")

    try:
        price = float(input("Enter item price: "))

        if price <= 0:
            print("Price must be greater than 0.")
        else:
            cart[item_name] = price
            print(item_name, "has been added to the cart.")

    except ValueError:
        print("Invalid price! Please enter a number.")


# Main program
while True:

    print("\n===== SHOPPING CART =====")
    print("1. Add item")
    print("2. View cart")
    print("3. Calculate total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Add item
    if choice == "1":
        add_item()

    # View cart
    elif choice == "2":

        if len(cart) == 0:
            print("Your cart is empty.")

        else:
            print("\nItems in your cart:")

            for item, price in cart.items():
                print(item, ":", price)

    # Calculate total
    elif choice == "3":

        total = sum(cart.values())

        print("Total bill: $", total)

    # Exit
    elif choice == "4":

        print("Thank you for shopping!")
        break

    # Invalid choice
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")