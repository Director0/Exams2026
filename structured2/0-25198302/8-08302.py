from itertools import *


cnt = 0

for p in product("01234", repeat=6):
    p1 = "".join(p)

    if p1[-1] != "3" and p1[-1] != "4" and p1[0] != "1" and p1[0] != "0":
        cnt += 1


print(cnt)