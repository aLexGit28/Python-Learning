# age = int(input('Enter your age: '))

# if age>=18:
#     print('You can vote as you are an adult.')
# else:
#     print('You are not eligible to vote right now.')

marks = int(input('Enter your marks scored: '))

if marks>=90:
    grade = 'A'
elif marks>=80 and marks<90:
    grade = 'B'
elif marks>=70 and marks<80:
    grade = 'C'
elif marks>=60 and marks<70:
    grade = 'D'
else:
    grade = 'F'
    
print('You got ', grade)