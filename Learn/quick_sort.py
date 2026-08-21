def quick_sort(arr):
  if len(arr) <= 1:
      return arr
  else:
      pivot = arr[0]
      less_than_pivot = [x for x in arr[1:] if x <= pivot]
      greater_than_pivot = [x for x in arr[1:] if x > pivot]
      return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

# Initial list
numbers = [51, 95, 66, 72, 42, 38, 39, 41, 15]

# Sorting the list
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
