from itertools import *


cnt = 0

for i in set(product("АБВГЭЮЯ", repeat=5)):
    i1 = "".join(i)

    i1 = i1.replace("Э", "*").replace("Ю", "*").replace("Я", "*")

    if i1[0] == "*" and i1[-1] == "*" and i1.count("*") == 2:
        cnt += 1


print(cnt)