from itertools import *

cnt = 0

for i in product("0123456789ABCDEFGHIJKLMNO", repeat=4):
    i1 = "".join(i)

    if (i1[0] != "0") and (len([x for x in i1 if x in "13579BDFHJLN"]) == 1) and (len([x for x in i1 if x in "012345"])) <= 2:
        cnt += 1

print(cnt)