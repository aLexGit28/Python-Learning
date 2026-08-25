from pickle import NONE

class Node():
  def __init__(self, data):
      self.data = data
      self.next = NONE

a = Node(10)
b = Node(20)
c =Node(40)

a.next = b
b.next =c
c.next = NONE

print(a.data)
print(a.next.data)
print(a.next.next.data)
