from itertools import *

gcnt = 0

for i in product("0123456789ABCDE", repeat=7):
    i1 = "".join(i)
    cnt = 0

    for q in "ABCDE":
        cnt += i1.count(q)

    if i1[0] != "0" and i.count("0") == 2 and cnt <= 3:
        gcnt += 1


print(gcnt)