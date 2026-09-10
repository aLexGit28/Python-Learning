class Bank:
    def __init__(self, balance):
        self.balance = balance

    def add_interest(self, rate):
        interest = self.balance * rate / 100
        self.balance = self.balance + interest

    def show_balance(self):
        print("Total Balance: ₹" + format(self.balance, ".2f"))


balance = float(input("Enter initial balance: "))
rate = float(input("Enter interest rate: "))

account = Bank(balance)
account.add_interest(rate)
account.show_balance()