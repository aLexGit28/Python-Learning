class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance = self.balance + interest

    def display_balance(self):
        print("Updated Balance:", self.balance)


# Taking input from the user
balance = float(input("Enter initial balance: "))
rate = float(input("Enter interest rate (%): "))

# Creating an object
account = BankAccount(balance)

# Calculating interest
account.calculate_interest(rate)

# Displaying updated balance
account.display_balance()