# h=int(input("Enter the height: "))#The user enters the input
# for i in range(1,h+1):#Outer loop running for h+1 rows
#     for j in range(1,h-i+1):#Inner loop running for h-i-1 columns
#         print(" ",end=" ")#Printing empty spaces
#     for j in range(1,i+1):#Inner loop running for i+1 columns
#         print('*',end=" ")#Printing stars
#     for j in range(1,i):#Inner loop running till i
#         print('*',end=" ")#Printing stars
#     print("\n")#Switching to next line

for i in range(1,5):
    for j in range(1, 4-i+1):
        print(' ', end=' ')
    for j in range(1, i+1):
        print('*', end=' ')
    for j in range(1,i):
        print('*', end=' ')
    print()
