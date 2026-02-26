from itertools import *

s1 = "56 4678 6 26 17 1234 25 2".split()
s2 = "АБ АЗ БВ ВГ ГЗ ЗЖ ЗЕ ЕГ ГД".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖЗ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)