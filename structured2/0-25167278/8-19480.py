from itertools import *

cnt = 0

for i in set(permutations("ПАРИЖАНКА")):
    i1 = "".join(i)

    for x in "АИ":
        i1 = i1.replace(x, "g")

    if i1.count("gg") == 1 and "ggg" not in i1:
        cnt += 1

print(cnt)