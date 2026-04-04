from itertools import *

s1 = "235 1347 125 27 1367 57 2456".split()
s2 = "АБ АВ АГ ГВ ГЕ ГД ДЕ ЕБ ЕЖ ЖБ БВ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)