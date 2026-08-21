# my_list = []

# my_list = list()

from re import M
from statistics import mean


my_list = [3, 4, 6, 'Oranges', 'bananas', 'Elephant', True, 3.22]

# print(my_list[4])
# print(my_list[-4])

my_list.pop()
print(my_list)

# print(len(my_list[5]))

# remove any element
# del my_list[4]

# print(my_list)

# # add elememt on the list at the end
# my_list.append('Apples')
# print(my_list)

# # replace an element
# my_list[3] = 'Strawberries'
# print(my_list)

# # using remove()

# my_list.remove(True)
# print(my_list)


new_list = [6, 8, 10, 12, 3, 6, 9, 0, -8, 54, -1, 48, 12]
print(new_list)

print(mean(new_list))

print(sum(new_list)/len(new_list))