from itertools import *

cnt = 0

for i in product("01234567", repeat=6):
    i1 = "".join(i)

    for x in "1357":
        i1 = i1.replace(x, "*")

    if i1[0] != "0" and i1.count("6") == 2 and "*6" not in i1 and "6*" not in i1:
        cnt += 1


print(cnt)