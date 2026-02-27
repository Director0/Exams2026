from itertools import *

num = 0

for i in product("ЕЛОЧЩЬ", repeat=6):
    i1 = "".join(i)

    num += 1

    for x in "ЛЧЩ":
        i1 = i1.replace(x, "g")

    if "Ь" in i1 and i1[0] != "Ь" and i1.count("g") <= 2:
        print(num, i1)