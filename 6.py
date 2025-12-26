# Exercise 6: Given a list and a value entered via the keyboard, count the number of times the value appears in the list.
numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon tim so luong: "))

counter = 0

for i in range(0, len(numbers)):
    if numbers[i] == value:
        counter += 1

print("Số đó xuất hiện", counter, "lần.")
