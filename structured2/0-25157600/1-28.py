from itertools import *

s1 = "246 1345 25 1267 237 147 456".split()
s2 = "АБ АВ АГ БГ БД ДГ ГВ ВЕ ЕК КД ЕД".split()

print(* range(1,10))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)