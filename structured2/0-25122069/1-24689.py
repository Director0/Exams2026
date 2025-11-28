from itertools import *

s1 = "2456 15 46 136 12 134".split()
s2 = "AB AC BD CD DE DF EF".split()

print(* range(1, 7))

for p in permutations("ABCDEF"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)