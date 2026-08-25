print("Grade Calculation for Priya")

try:
    mark1 = int(input("Enter mark 1: "))
    mark2 = int(input("Enter mark 2: "))
    mark3 = int(input("Enter mark 3: "))

    marks = [mark1, mark2, mark3]

    average = sum(marks) / 3

    print("Marks:", marks)
    print("Average:", average)

    if average >= 90:
        grade = "A"

    elif average >= 80:
        grade = "B"

    elif average >= 70:
        grade = "C"

    else:
        grade = "D"

    print("Grade:", grade)

except ValueError:
    print("Please enter numbers only!")