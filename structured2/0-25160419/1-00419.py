from itertools import *

s1 = "268 1346 2458 237 378 127 456 135".split()
s2 = "АВ АБ БГ БК КГ КИ ИД ИЕ ЕД ЕА ВД ВГ ГД".split()

print(* range(1,10))

for p in permutations("АБВГДЕИК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)