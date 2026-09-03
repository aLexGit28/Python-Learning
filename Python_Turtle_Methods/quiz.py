import time
import random

def create_question():
    operators = ('+', '-', '/', '*')
    operator = random.choice(operators)

    if operator == '+':
        num1 = random.randint(1,1000)
        num2 = random.randint(1,1000)
        question = str(num1)+operator+str(num2)
        return question
    
    elif operator == '-':
        num1 = random.randint(1,1000)
        num2 = random.randint(0, num1)
        question = str(num1)+operator+str(num2)
        return question
    
    elif operator == '/':
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 10)
        question = str(num1)+operator+str(num2)
        return question
    
    elif operator == '*':
        num1 = random.randint(1, 100)
        num2 = random.randint(1,10)
        while num1 % num2 != 0:
            num1 = random.randint(1, 100)
            num2 = random.randint(1,10)
        question = str(num1)+operator+str(num2)
        return question        


def get_answers(question):
    answer = eval(question)
    return answer


score = 0

start = time.time()

for i in range(10):
    print()
    question = create_question()
    print("Question #", i+1, " :")
    print(question)
    print()
    user_answer = input("Enter your answer: ")
    print()

    if user_answer == "":
        pass

    else:
        try:
            user_answer = float(user_answer)

            if user_answer == get_answers(question):
                score += 4

        except ValueError:
            print("Invalid input: no score change.")
    
end = time.time()

duration = end - start
minutes = int(duration/60)
seconds = int(duration%60)

print(f"Your score: {score}/40")
print(f"Time taken: {minutes} minutes and {seconds} seconds")

