def DemSoLuong(x, lstX):
    dem = 0
    for y in lstX:
        if x == y:
            dem += 1
    return dem
