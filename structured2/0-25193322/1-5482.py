from itertools import *

s1 = "56 4568 78 2578 1246 125 348 2347".split()
s2 = "АЕ АГ ГЕ АБ БГ БЖ ЖИ ЖГ ЖД ДИ ИВ ВД ДБ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖИ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)

        