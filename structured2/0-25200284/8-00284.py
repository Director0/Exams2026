from itertools import *


cnt = 0

for i in product("012345678", repeat=7):
    i1 = "".join(i)

    if i1[0] != "0" and all(i1[0] != x for x in "1357") and any(i1[-1] == x for x in "0124578") and i1.count("6") >= 1:
        cnt += 1


print(cnt)