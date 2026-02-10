from itertools import *

num = 0
cnt = 0

for i in product("АЖЗОПЮ", repeat=6):
    num += 1
    i1 = "".join(i)

    if num % 2 == 0 and i1[0] == "А" and i1.count("З") >= 2:
        print(i1)
        cnt += 1

print(cnt)
