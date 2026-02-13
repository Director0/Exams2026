from itertools import *

s1="457 37 267 1678 16 3458 12348 467".split()
s2 = "АБ АВ АГ ГВ ГЖ ГЕ ГЗ ВЖ ВД ЖД ДЕ ЕЗ БД".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖЗ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)