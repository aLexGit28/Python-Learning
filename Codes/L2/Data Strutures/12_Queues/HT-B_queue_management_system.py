class QueueManagement:

    def __init__(self):
        self.queue = []

    # Add a person to the queue
    def enqueue(self, person):
        self.queue.append(person)
        print(person, "joined the queue.")

    # Serve the first person in the queue
    def dequeue(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            person = self.queue.pop(0)
            print(person, "has been served.")

    # Show the first person in the queue
    def peek(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("Next person to be served:", self.queue[0])

    # Check whether the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display everyone in the queue
    def show_queue(self):
        if self.is_empty():
            print("The queue is empty.")
        else:
            print("\nPeople currently in the queue:")
            for person in self.queue:
                print("-", person)
                
# testing the QueueManagement class
bank_queue = QueueManagement()

bank_queue.enqueue("Rahul")
bank_queue.enqueue("Priya")
bank_queue.enqueue("Amit")
bank_queue.enqueue("Sneha")

bank_queue.show_queue()

bank_queue.peek()

bank_queue.dequeue()

bank_queue.show_queue()

bank_queue.peek()