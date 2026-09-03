import random
import time

score = 0

print("Welcome to the Mathematics Competition!")
print("You will get 10 questions.")
print()

start_time = time.time()

for i in range(10):

    num1 = random.randint(100, 999)
    num2 = random.randint(100, 999)

    operation = random.choice(["+", "-"])

    print("Question", i + 1, ":", num1, operation, num2)

    answer = int(input("Enter your answer: "))

    if operation == "+":
        correct_answer = num1 + num2
    else:
        correct_answer = num1 - num2

    if answer == correct_answer:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")
        print("Correct answer is:", correct_answer)

    print()

end_time = time.time()

total_time = end_time - start_time

print("Competition Finished!")
print("----------------------")
print("Your Score:", score, "/ 10")
print("Time Taken:", round(total_time, 2), "seconds")