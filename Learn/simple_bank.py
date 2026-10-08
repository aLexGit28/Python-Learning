balance = 1000


def deposit():
    global balance

    amount = int(input("Enter amount: "))
    balance = balance + amount

    print("Current Balance:", balance)


def withdraw():
    global balance

    amount = int(input("Enter amount: "))

    if amount <= balance:
        balance = balance - amount
        print("Current Balance:", balance)
    else:
        print("Insufficient Balance")


def banking():
    while True:

        print("\n1.Deposit   2.Withdraw   3.Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            deposit()

        elif choice == 2:
            withdraw()

        elif choice == 3:
            break

        else:
            print("Invalid choice")


banking()