from itertools import *

s1 = "25 137 267 56 146 345 23".split()
s2 = "АБ АВ БВ ВЕ ЕЖ ЕД ЖД ДГ ГА".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)