from itertools import *

num = 0

for i in product("ЕИОРТЯ", repeat = 6):
    num += 1
    i1 = "".join(i)

    if num % 2 != 0 and i1[0] not in "РТЯ" and i1.count("И") >= 2:
        print(num, i1)
        