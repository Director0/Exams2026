from itertools import *

s1 = "567 357 246 36 127 134 125".split()
s2 = "АБ АВ ВБ ВЕ ЕГ ЕК КГ КД ДГ ДБ".split()

print(* range(1, 9))

for p in permutations("АБВГДЕК"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)