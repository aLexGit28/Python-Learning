# mySet = {'Ikjot', True, 7, 'Ikjot', 16, True, 16, 'Dragon Fruit'}

# print(mySet)

# print(myNumSet)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.union(y) 
z_intersection = x.intersection(y)
print(z)    
print(z_intersection)
#set difference
z_difference = x.difference(y)
print(z_difference)

z_difference_y = y.difference(x)
print(z_difference_y)

z_symmetric_difference = x.symmetric_difference(y)
print(z_symmetric_difference)