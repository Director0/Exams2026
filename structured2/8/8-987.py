from itertools import *

cnt = 0

for i in permutations("КОБУРА"):
    i1 = "".join(i)

    for g in "УА":
        i1 = i1.replace(g, "О")

    for g in "БР":
        i1 = i1.replace(g, "К")

    if "КК" not in i1 and "ОО" not in i1:
        cnt += 1

print(cnt)