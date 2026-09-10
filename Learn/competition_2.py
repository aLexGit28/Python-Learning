import random
import time

score = 0
start = time.time()

for i in range(1, 11):

    num1 = random.randint(10, 999)
    num2 = random.randint(1, 999)

    operator = random.choice(["+", "-", "*", "/"])

    if operator == "+":
        answer = num1 + num2

    elif operator == "-":
        answer = num1 - num2

    elif operator == "*":
        answer = num1 * num2

    else:
        num1 = num1 - (num1 % num2)
        if num1 == 0:
            num1 = num2
        answer = num1 // num2

    print("\nQuestion", i, ":")
    print(num1, operator, num2)

    user_answer = int(input("Enter your answer : "))

    if user_answer == answer:
        score += 1

end = time.time()

total_time = int(end - start)
minutes = total_time // 60
seconds = total_time % 60

print("\nYour Score :", score, "/ 10")
print("Time Taken :", minutes, "Minutes and", seconds, "Seconds")