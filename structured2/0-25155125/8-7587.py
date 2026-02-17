from itertools import *

num = 0

for i in product("АВЛОР", repeat=4):
    num += 1
    i1 = "".join(i)

    if i1[0] == "Л":
        print(num)
        break