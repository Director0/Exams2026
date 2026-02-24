from itertools import *

s1 = "358 78 16 57 146 35 248 127".split()
s2 = "АД АГ ДЕ ДБ ЕБ БВ ВГ ВК КЖ ЖГ БД".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)