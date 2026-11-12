mylist = ['strawberry', 'mango', 'iphone', 'clash royale', 18]
print(type(mylist))
my_tuple = ('basket', 'apple', 27, 'mountain')

mylist = tuple(mylist)
print(type(mylist))

result = mylist+my_tuple
print(result)