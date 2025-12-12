from itertools import *

s1 = "235 14 1456 236 1367 3457 56".split()
s2 = "КР КП РТ РС СТ СЛ СМ МЛ ЛТ ЛП ПТ".split()

print(* range(1, 7))

for p in permutations("КПРТСЛМ"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)