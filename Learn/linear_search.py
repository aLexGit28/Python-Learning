def linear_search(arr, target):
  for index, value in enumerate(arr):
    if value==target:
      return index
  return -1

n = int(input('Enter the number of elements in the array: '))

a=[0] * n
for i in range(n):
  a[i] = int(input('Enter the value: '))

x = int(input('Enter the element to be searched: '))

if linear_search(a, x) == -1:
  print(f'{x} is not found in array {a}.')
else:
  print(f'{x} is found at index {linear_search(a, x)}')