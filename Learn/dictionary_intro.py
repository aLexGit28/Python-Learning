captials = {"France": "Paris", "Germany": "Berlin", "Italy": "Rome", "Spain": "Madrid", "Portugal": "Lisbon"}

print(captials)
print(captials['Spain'])

print(captials.items())
print(captials.keys())
print(captials.values())

# students = {1: "Alice", 2: "Bob", 3: "Charlie", 4: "David"}
# print(students[1])

# print(students[4])

# Nested dictionary
students = {1: {"name": "Alice", "age": 20, "major":    "Computer Science"},
    2: {"name": "Bob", "age": 22, "major": "Mathematics"},
    3: {"name": "Charlie", "age": 21, "major": "Physics"},
    4: {"name": "David", "age": 23, "major": "Chemistry"}}
    
print(students[2]["major"])
