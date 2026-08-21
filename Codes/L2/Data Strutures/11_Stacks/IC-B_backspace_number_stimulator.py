class BackspaceNumber:

    def __init__(self):
        self.stack = []

    # Add digits to the stack
    def enter_number(self, number):
        for digit in number:
            self.stack.append(digit)

    # Remove the last digit
    def backspace(self):
        if self.is_empty():
            print("No digits left!")
        else:
            self.stack.pop()

    # Display the current number
    def display_number(self):
        if self.is_empty():
            print("The number is empty.")
        else:
            print("After backspace, the number becomes:", "".join(self.stack))

    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

# testing the BackspaceNumber class
number = input("Enter a number: ")

keyboard = BackspaceNumber()

keyboard.enter_number(number)

keyboard.backspace()

keyboard.display_number()