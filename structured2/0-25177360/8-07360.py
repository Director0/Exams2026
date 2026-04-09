from itertools import *

num = 0

for i in product("АВИКНСТ", repeat=4):
    i1 = "".join(i)

    if i[0] in "ВКНСТ" and i[-1] in "АИ":
        num += 1

        if i1 == "НИКА":
            print(num, i1)