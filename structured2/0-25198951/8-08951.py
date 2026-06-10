from itertools import *

cnt = 0

for i in set(permutations("КОМЕТА", r=6)):
    i1 = "".join(i)

    for x in "ОЕА":
        i1 = i1.replace(x, "*")

    for x in "КМТ":
        i1 = i1.replace(x, "$")

    if "**" not in i1 and "$$" not in i1:
        cnt += 1

print(cnt)