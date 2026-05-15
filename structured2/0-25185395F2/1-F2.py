from itertools import *

print(*range(1, 10))

s1 = "27 1567 67 5 246 2357 1236".split()
s2 = "АБ БВ ВД ВЕ ВГ ГЕ ЕД ЕК КД ДБ".split()

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)