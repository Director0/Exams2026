from itertools import *

cnt = 0

for i in product("0123456789ABCDEF", repeat=4):
    i1 = "".join(i)

    if i1[0] != "0" and i1.count("9") == 1 and (all(f"{x}{x}" not in i1 for x in "02468ACE") or all(f"{x}{x}" not in i1 for x in "13579BDF")):
        cnt += 1
        print(i1)


print(cnt)