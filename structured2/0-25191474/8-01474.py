from itertools import *


cnt = 0

for p in set(permutations("АМФИБРАХИЙ")):
    p1 = "".join(p)

    if p1[4:6] == "БР":
        print(p1)
        cnt += 1


print(cnt)