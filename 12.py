# Exercise 12: Given a list of numbers, sort the elements in descending order.
numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

# numbers.sort()
# DescendingNumber = numbers[::-1]
# print(DescendingNumber)

numbers.sort(reverse=True)
print(numbers)
