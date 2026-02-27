from itertools import *

cnt = 0

for i in product("0123456789ABC", repeat=7):
    i1 = "".join(i)

    if i1[0] != "0" and i1.count("5") >= 2:
        for x in "02468AC":
            i1 = i1.replace(x, "X")

        for x in "13579B":
            i1 = i1.replace(x, "Y")

        if "XX" not in i1 and "YY" not in i1:
            cnt += 1


print(cnt)