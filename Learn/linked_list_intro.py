class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(10)
b = Node(20)
c = Node(40)

a.next = b # pyright: ignore[reportAttributeAccessIssue]
b.next = c # pyright: ignore[reportAttributeAccessIssue]
c.next = None

print(a.data)
print(a.next.data) # type: ignore
print(a.next.next.data) # type: ignore