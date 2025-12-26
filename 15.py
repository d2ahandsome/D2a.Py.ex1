# Exercise 15: Given a list, count and display the number of occurrences of each value in the list.
from collections import Counter

A = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

counts = Counter(A)
for value, times in counts.items():
    print(value, ":", times)
