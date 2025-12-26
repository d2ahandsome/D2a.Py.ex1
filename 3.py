# Exercise 3: Given a list and a value entered via the keyboard, determine whether the value exists in the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

x = int(input("Nhập giá trị muốn tìm: "))

if x in numbers:
    print("Có nhé bro")
else:
    print("Không có đâu")