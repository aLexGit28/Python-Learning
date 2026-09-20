n = int(input("Enter a number: "))

flag=0
for i in range(2, n):
    if n%i == 0:
        flag=1
        break

if flag==1:
    print("Its not a prime no.")
else:
    print("Its a prime no.")