n = int(input("Enter number of rows: "))

# Top half
for i in range(1, n + 1):
    print("*" * i, end="")

    spaces = 2 * (n - i) - 1

    if spaces > 0:
        print(" " * spaces, end="")
        print("*" * i)
    else:
        print()

# Bottom half
for i in range(n - 1, 0, -1):
    print("*" * i, end="")

    spaces = 2 * (n - i) - 1

    if spaces > 0:
        print(" " * spaces, end="")
        print("*" * i)
    else:
        print()