from itertools import *


cnt = 0

for i in permutations("АКПРЫ", r=5):
    i1 = "".join(i)

    for x in "АЫ":
        i1 = i1.replace(x, "*")

    if i1[0] != "Р" and i1[-1] != "Р" and "**" not in i1:
        print(i1)
        cnt += 1


print(cnt)