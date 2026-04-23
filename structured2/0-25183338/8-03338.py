from itertools import *

cnt = 0

for i in set(permutations("АМФИБРАХИЙ")):
    i1 = "".join(i)

    if i1[4:6] == "БР":
        print(i1)
        cnt += 1


print(cnt)