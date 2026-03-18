from itertools import *

s1 = "47 4567 5 12 237 2 125".split()
s2 = "АБ БВ БГ ГВ ГЖ ЖД ДВ ВЕ".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)