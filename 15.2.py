#Exercise 15: Given a list, count and display the #import method DemSoLuong from MyMethod.py
from MyMethod import *
#Solution 2:
lstA= [5, 7, 8, 9, 10, 20, 15, 8, 7, 4, 3, 8, 10, 15, 17, 19]
lstB = []
lstC = []

for x in lstA:
    if x not in lstB:
        count = DemSoLuong (x,lstA) #Count
        lstB.append(x)
        lstC.append(count)
print(lstB)
print(lstC)