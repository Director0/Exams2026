from itertools import *

num = 0

for i in product("ВИЛМОС", repeat=5):
    num += 1
    i1 = "".join(i)

    if (num % 2 != 0) and (i1[0] != "О" and i1[0] != "С") and i1.count("В") == 1 and i1.count("С") <= 1:
        print(num, i1)