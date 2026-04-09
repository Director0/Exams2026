from itertools import *

s1 = "256 1458 478 237 126 158 348 2367".split()
s2 = "АВ АБ АГ ГБ ГД ГЖ ЖЕ ЖЗ ЗЕ ЗД ЕД ДВ ДГ ВБ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖЗ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)