from itertools import *

s1 = "278 18 58 58 348 78 168 1234567".split()
s2 = "АБ АВ АГ БГ ВГ ГЕ ГЗ ГЖ ГД ДЖ ЖЗ ЕЗ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖЗ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)

