name = input("Enter friend's name: ")
phone = input("Enter phone number: ")

file = open("contacts.txt", "a")

file.write("Name: " + name + "\n")
file.write("Phone: " + phone + "\n")
file.write("--------------------\n")

file.close()

print("Contact saved successfully!")