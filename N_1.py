from itertools import *

s1 = "457 358 2458 1367 123 478 146 236".split()
s2 = "АБ АГ АЕ БВ БД ВД ВИ ГД ГЕ ГЖ ДИ ЕЖ ЖИ".split()

print(* range(1,9))

for p in permutations("АБВГДЕЖИ"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)
