from itertools import *

s1 = "3456 3567 126 17 127 123 245".split()
s2 = "АБ АД ДВ ВБ БГ ГВ ГЕ ГК КЕ КД ЕД".split()

print(* range(1,10))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)