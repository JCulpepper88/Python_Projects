numbers = [5, 7, 2, 8, 1, 9, 3]
biggest = max(numbers)
print(biggest)


numbers = [4, 6, 1, 7, 3, 9, 8, 13, 2]
number = numbers[0]
for i in numbers:
    if i > number:
        number = i
index = numbers.index(number)
print(f"The highest number in the list is '{number}', which is at location '{index}'")
