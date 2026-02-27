from itertools import *

s1 = "2345 1367 124 1357 147 2 245".split()
s2 = "ПМ ПР ПС ПЛ СР РК РМ МК КЛ СЛ ЛТ".split()

print(* range(1,10))

for p in permutations("ПСЛТМРК"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)