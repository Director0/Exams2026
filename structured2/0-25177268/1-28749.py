from itertools import *

s1 = "457 346 24 123 167 257 156".split()
s2 = "АБ АВ БВ ВЕ ЕГ ЕК КГ КД ГД ДБ".split()

print(* range(1,10))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)