from itertools import *

cnt = 0

for i in product("0123456789ABCD", repeat=5):
    i1 = "".join(i)
    print(i1)

    for x in "ABCD":
        i1 = i1.replace(x, "*")

    for x in "13579":
        i1 = i1.replace(x, "+")

    if i1[0] != "0" and "*+" not in i1 and "+*" not in i1:
        cnt += 1
        # print(i1)


print(cnt)