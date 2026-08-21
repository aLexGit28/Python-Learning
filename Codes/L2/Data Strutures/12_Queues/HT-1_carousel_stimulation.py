class Carousel:

    def __init__(self):
        self.line = []

    # Add a child to the line
    def join_line(self, name):
        self.line.append(name)
        print(name, "joined the line.")

    # Give the first child a turn
    def take_ride(self):
        if self.is_empty():
            print("No children are waiting for the ride.")
        else:
            child = self.line.pop(0)
            print(child, "is now riding the carousel!")

    # Show the child who will ride next
    def peek(self):
        if self.is_empty():
            print("The line is empty.")
        else:
            print("Next child:", self.line[0])

    # Check if the line is empty
    def is_empty(self):
        return len(self.line) == 0

    # Show everyone waiting in line
    def show_line(self):
        if self.is_empty():
            print("The line is empty.")
        else:
            print("\nChildren waiting in line:")
            for child in self.line:
                print("-", child)
                
# testing the Carousel class
carousel = Carousel()

carousel.join_line("Mary")
carousel.join_line("Rahul")
carousel.join_line("Priya")
carousel.join_line("Amit")

carousel.show_line()

carousel.peek()

carousel.take_ride()

carousel.show_line()

carousel.take_ride()

carousel.peek()