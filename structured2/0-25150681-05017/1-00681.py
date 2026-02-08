from itertools import *

s1="57 78 68 578 1467 358 1245 2346".split()
s2 = "АЕ АЖ ЕЖ ЕГ ЕД ДЗ ДБ БЗ ЗГ ЗВ ВЖ ЖГ".split()

print(* range(1,10))

for p in permutations("АЕЖГЗВДБ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)