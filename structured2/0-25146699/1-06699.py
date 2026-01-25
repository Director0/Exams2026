from itertools import *

s1="256 13467 2456 237 136 1235 24".split()
s2 = "АБ АГ БГ БД БЕ ЕД ЕЖ ЖД ДГ ДВ ВГ ВА".split()

print(* range(1,10))

for p in permutations("АБВГДЕЖ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)