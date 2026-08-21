def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


# Driver Code
n = int(input("Enter the number of elements: "))

arr = []

print("Enter the elements in sorted order:")
for i in range(n):
    arr.append(int(input()))

target = int(input("Enter the element to search: "))

result = binary_search(arr, target)

if result == -1:
    print(f"{target} is not found in the array.")
else:
    print(f"{target} is found at index {result}.")