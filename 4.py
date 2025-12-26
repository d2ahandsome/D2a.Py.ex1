#Exercise 4: Given a list and a value entered via the keyboard, determine whether the value exists in the list. If it does, return the index of its first occurrence
numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon tim: "))

if value in numbers:
    firstIndex = numbers.index(value)
    print("Vị trí số đó xuất hiện lần đầu là:", firstIndex)
else:
    print("Không có số đó")