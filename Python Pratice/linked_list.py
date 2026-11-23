
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Add a node to the linked list
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node

    # Display the linked list
    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            temp = self.head
            print("Linked List:")

            while temp is not None:
                print(temp.data, end=" ")
                temp = temp.next

            print()

    # Delete a node by value
    def delete(self, value):
        temp = self.head

        # Check if the first node needs deletion
        if temp is not None and temp.data == value:
            self.head = temp.next
            print("Node with value", value, "deleted successfully.")
            return

        # Search for the node
        prev = None

        while temp is not None and temp.data != value:
            prev = temp
            temp = temp.next

        # Value not found
        if temp is None:
            print("Node not found.")
            return

        # Remove the node
        prev.next = temp.next
        print("Node with value", value, "deleted successfully.")


# Create linked list
ll = LinkedList()

# Insert initial values
for i in [1, 2, 3, 4, 5]:
    ll.append(i)

# Menu-driven program
while True:
    print("\nWhat would you like to do?")
    print("1. Display the linked list")
    print("2. Delete a node by value")
    print("3. Exit")

    choice = int(input("Enter your choice (1-3): "))

    if choice == 1:
        ll.display()

    elif choice == 2:
        value = int(input("Enter the value of the node to delete: "))
        ll.delete(value)

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")
