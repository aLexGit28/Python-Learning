class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def find_cheapest(root):
    if root.left is None:
        return root.value

    return find_cheapest(root.left)


# Create the BST
root = None

prices = [500, 200, 800, 100, 300, 600, 900]

for price in prices:
    root = insert(root, price)

# Find the cheapest product
print("Cheapest price:", find_cheapest(root))