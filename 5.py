 #Exercise 5: Given a list and a value entered via the keyboard, determine whether the value exists in the list. If it does, return the index of its last occurrence.
numbers = [1, 2, 3, 2, 4, 3, 5, 8, 6, 7, 8]

value = int(input("Nhap so muon tim: "))

lastIndex = -1
for i in range(0, len(numbers)):
    if numbers[i] == value:
        lastIndex = i

if lastIndex != -1:
    print("Vị trí số đó xuất hiện lần cuối là:", lastIndex)
else:
    print("Không có số đó")