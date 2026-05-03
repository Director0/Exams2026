from itertools import *


cnt = 0

for i in set(product("0123456789AB", repeat=5)):
    i1 = "".join(i)

    for x in "13579B":
        i1 = i1.replace(x, "*")

    if i1.count("**") <= 2:
        cnt += 1

print(cnt)