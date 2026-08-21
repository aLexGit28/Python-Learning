class ToyBox:

    def __init__(self):
        self.stack = []

    # Add a toy to the box
    def add_toy(self, toy):
        self.stack.append(toy)
        print(toy, "was added to the toy box.")

    # Take the last toy out
    def take_toy(self):
        if self.is_empty():
            print("The toy box is empty!")
        else:
            toy = self.stack.pop()
            print(toy, "was taken out.")

    # Look at the top toy
    def peek(self):
        if self.is_empty():
            print("The toy box is empty!")
        else:
            print("Top toy:", self.stack[-1])

    # Check whether the box is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Show all toys
    def show_toys(self):
        if self.is_empty():
            print("The toy box is empty!")
        else:
            print("\nToys in the box:")
            for toy in self.stack:
                print("-", toy)