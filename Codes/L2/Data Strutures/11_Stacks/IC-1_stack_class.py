class Stack:

    def __init__(self):
        self.stack = []

    # Add a topic to the stack
    def push(self, topic):
        self.stack.append(topic)
        print(topic, "was added to the stack.")

    # Remove the top topic
    def pop(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            topic = self.stack.pop()
            print(topic, "was revised and removed.")

    # Show the top topic
    def peek(self):
        if self.is_empty():
            print("The stack is empty.")
        else:
            print("Next topic to revise:", self.stack[-1])

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    
# testing the Stack class
topics = Stack()

# Add topics while studying
topics.push("Python Basics")
topics.push("Lists")
topics.push("Loops")
topics.push("Functions")

print()

# Check which topic is on top
topics.peek()

print()

# Revise topics in reverse order
topics.pop()
topics.pop()
topics.pop()
topics.pop()

print()

# Check whether all topics are completed
if topics.is_empty():
    print("All topics completed! Toshini is ready for her examination!")