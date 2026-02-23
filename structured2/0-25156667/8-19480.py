from itertools import *

cnt = 0

for i in set(permutations("ПАРИЖАНКА")):
    i1 = "".join(i)

    for x in "ИА":
        i1 = i1.replace(x, "*")

    if i1.count("**") == 1 and "***" not in i1:
        cnt += 1


print(cnt)