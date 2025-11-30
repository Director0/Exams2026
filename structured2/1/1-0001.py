from itertools import *

s1 = "2357 167 145 357 13467 257 12456".split()
s2 = "KQ QA QC KA AC AR AB KP PR PB RB KB".split()

print(* range(1, 9))

for p in permutations("ABCQKRP"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)