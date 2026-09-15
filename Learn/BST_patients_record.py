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


def search(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if data < root.data:
        return search(root.left, data)
    else:
        return search(root.right, data)


def delete(root, data):
    if root is None:
        return None

    if data < root.data:
        root.left = delete(root.left, data)
    elif data > root.data:
        root.right = delete(root.right, data)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = root.right
        while temp.left:
            temp = temp.left

        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root


# Patient IDs
root = None

root = insert(root, 101)
root = insert(root, 205)
root = insert(root, 150)
root = insert(root, 99)

print("Patient IDs added")

# Search
print("Search ID: 150")

if search(root, 150):
    print("Found")
else:
    print("Not Found")

# Delete
print("Remove ID: 101")
root = delete(root, 101)
print("Removed!")