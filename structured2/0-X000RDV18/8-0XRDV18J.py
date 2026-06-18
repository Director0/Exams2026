from itertools import *
from string import printable

num = 0
for i in product("ABDLMRU", repeat=8):
    num += 1
    i1 = "".join(i)

    if i1[-1] == "A" and i1[0] == "B" and i1.count("A") == 2 and printable[56] in i1:
        print(num, i1)