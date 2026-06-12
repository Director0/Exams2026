from itertools import *

s1 = "2457 136 2567 16 137 234 135".split()
s2 = "АБ АД БВ ВД ДЕ ДК ЕК ЕГ КГ ГВ ГБ".split()

print(*range(1, 10))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)