# Exercise 9: Given a list, create and output a set containing only the unique (non-repeating) elements of the list.
numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

unique_set = {x for x in numbers if numbers.count(x) == 1}

print("Set cac phan tu khong lap:", unique_set)