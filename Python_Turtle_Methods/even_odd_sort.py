def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers

    pivot = numbers[0]

    even = []
    odd = []

    for x in numbers[1:]:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)

    return even + [pivot] + odd


numbers = []

for i in range(5):
    num = int(input("Num: "))
    numbers.append(num)

even = []
odd = []

for x in numbers:
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)

result = even + odd

print("Even→Odd Sorted:", result)