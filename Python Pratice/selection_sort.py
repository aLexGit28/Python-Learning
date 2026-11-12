def selection_sort(numbers):
  n = len(numbers)
  total_comparisons = 0
  total_swaps = 0

  for i in range(n):
      min_index = i
      for j in range(i+1, n):
          total_comparisons += 1
          if numbers[j] < numbers[min_index]:
              min_index = j
      if min_index != i:
          numbers[i], numbers[min_index] = numbers[min_index], numbers[i]
          total_swaps += 1
      print(f"Iteration {i+1}: {numbers} (Comparisons: {i+1}, Swaps: {total_swaps})")

  print("\nSorted List:", numbers)
  print("Total Comparisons:", total_comparisons)
  print("Total Swaps:", total_swaps)

# Initial list
numbers = [29, 72, 98, 13, 87, 66, 52, 51, 36]

# Sorting the list
selection_sort(numbers)

