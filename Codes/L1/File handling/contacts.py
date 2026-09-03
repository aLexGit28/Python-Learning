file = open("Contacts.txt","w")
for i in range(1,3):
        name = input("Enter name: ")
        phone = input("Enter the phone number: ")
        file.write("Name: "+ name + "\n")
        file.write("Phone number: "+ phone + "\n")
file.close()
print("Contacts saved")