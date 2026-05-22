from itertools import *
from re import *

cnt = 0

for i in product("0123456789ABCDEF", repeat=15):
    i1 = "".join(i)

    for x in "02468ACE":
        i2 = i1.replace(x, "*")

    for x in "13579BDF":
        i2 = i1.replace(x, "$")

    if i1[0] != "0" and (i2 == "*$*$*$*$*$*$*$*" or i2 == "$*$*$*$*$*$*$*$") and i1 == sorted(i1, reverse=True):
        print(i1, sorted(i1, reverse=True))
        cnt += 1


print(cnt)