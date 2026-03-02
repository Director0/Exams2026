from itertools import *

s1 = "67 346 24 235 47 127 156".split()
s2 = "КЕ КА АЕ АБ БВ БГ ВГ ГД ДЕ".split()

print(* range(1,10))

for p in permutations("КАЕДБГВ"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)