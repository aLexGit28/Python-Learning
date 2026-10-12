def getIndex(numbers, value):
    low = 0
    high = len(numbers) - 1

    while low <= high:
        mid = (low + high) // 2

        if numbers[mid] == value:
            numbers.pop(mid)
            return mid
        elif numbers[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    return -1


numbers = [2, 3, 4, 5, 40]
value = 5

index = getIndex(numbers, value)

if index != -1:
    print("Element found at index", index,
          "and the list after removal is:", numbers)
else:
    print("Element not found!")