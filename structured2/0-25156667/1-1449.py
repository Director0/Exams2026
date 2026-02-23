from itertools import *

s1="24 146 56 1267 36 23457 46".split()
s2 = "АБ АВ ВБ ВД ВГ ГЕ ГК ЕК ЕВ ЕД".split()

print(* range(1,10))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)