class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):

    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def search(root, seat):

    if root is None:
        return False

    if root.data == seat:
        return True

    if seat < root.data:
        return search(root.left, seat)
    else:
        return search(root.right, seat)


# Create the BST
root = None

n = int(input("Total seats to enter: "))

for i in range(n):
    seat = input("Seat ID: ")
    root = insert(root, seat)


# Search for a seat
seat = input("Search Seat: ")

if search(root, seat):
    print("Booked")
else:
    print("Available")