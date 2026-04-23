from itertools import *

s1 = "2467 1357 25 156 2346 145 12".split()
s2 = "АБ АВ АГ БВ ВГ ГД ГЕ ЕД ЕБ ЕЖ ЖБ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        rint(*p)