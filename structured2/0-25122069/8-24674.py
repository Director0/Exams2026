from itertools import *

cnt = 0

for i in product("0123456789AB", repeat=6):
    i1 = "".join(i)
    i2 = set(i1)
    i3 = []

    for n1 in i2:
        if i1.count(n1) >= 2:
            i3.append(i1.count(n1))

    if i1[0] == i1[-2] and len(i3) == 1 and i3[0] == 2:
        cnt +=1

print(cnt)