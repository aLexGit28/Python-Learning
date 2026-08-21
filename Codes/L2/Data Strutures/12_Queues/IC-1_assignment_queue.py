class AssignmentQueue:

    def __init__(self):
        self.queue = []

    # Add a new assignment
    def enqueue(self, assignment):
        self.queue.append(assignment)
        print(assignment, "added to the queue.")

    # Show the oldest assignment
    def peek(self):
        if self.isEmpty():
            print("No assignments in the queue.")
        else:
            print("Oldest assignment:", self.queue[0])

    # Remove the oldest assignment
    def dequeue(self):
        if self.isEmpty():
            print("No assignments to complete.")
        else:
            completed_assignment = self.queue.pop(0)
            print(completed_assignment, "has been completed and removed.")

    # Check if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0