file = open("contacts.txt", "w")

for i in range(2):
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    file.write("Name: " + name + "\n")
    file.write("Phone: " + phone + "\n")

file.close()

print("Contacts saved")