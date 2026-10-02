letters = []
for i in range(1,6):
    alphabet = input(f"Enter alphabet {i}: ")
    letters.append(alphabet)
#print(letters)
print()
print("Choose a pattern: ")
print("1 - Half pyramid\n2 - Right Angle Triangle")
choice = int(input("\nEnter 1 or 2: "))
if choice == 1:
    print("\nHalf Pyramid Pattern")
    for i in range(5):
        for j in range(i+1):
            print(letters[j], end=" ")
        print()
        
elif choice == 2:
    print("\nRight Angle Triangle")
    for i in range(5):
        print("  " * (4 - i), end="")

        for j in range(i + 1):
            print(letters[j], end=" ")

        print()

else:
    print("Invalid Input")