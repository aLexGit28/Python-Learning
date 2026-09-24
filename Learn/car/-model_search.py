class Node:
    def __init__(self, model, price):
        self.model = model
        self.price = price
        self.left = None
        self.right = None


def insert(root, model, price):
    if root is None:
        return Node(model, price)

    if model < root.model:
        root.left = insert(root.left, model, price)
    else:
        root.right = insert(root.right, model, price)

    return root


def search(root, model):
    if root is None:
        return None

    if root.model == model:
        return root.price

    if model < root.model:
        return search(root.left, model)
    else:
        return search(root.right, model)


# Create the car tree
root = None

root = insert(root, "BMW", 5000000)
root = insert(root, "Audi", 4500000)
root = insert(root, "Honda", 1500000)
root = insert(root, "Toyota", 2000000)
root = insert(root, "Mercedes", 6000000)


# Search for a car
model = input("Enter car model: ")

price = search(root, model)

if price is not None:
    print("Car Model:", model)
    print("Price:", price)
else:
    print("Car model not found.")