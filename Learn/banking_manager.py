accounts = []
transaction_queue = []

number_of_accounts = int(input("Number of accounts: "))

# Add accounts
for i in range(number_of_accounts):

    account_number = int(input("Account number: "))
    name = input("Name: ")
    balance = float(input("Balance: "))

    account = [account_number, name, balance]
    accounts.append(account)


# Display accounts
print("\nAccounts:")

for account in accounts:

    print("Account number:", account[0])
    print("Name:", account[1])
    print("Balance:", account[2])
    print()


# Search account
search_number = int(input("Enter account number to search: "))

found = False

for account in accounts:

    if account[0] == search_number:

        print("Account found:", account[1])
        print("Balance:", account[2])

        transaction_queue.append(
            "Accessed account " + str(search_number)
        )

        found = True
        break


if found == False:
    print("Account not found")


# Display transaction queue
print("Transaction queue:", transaction_queue)