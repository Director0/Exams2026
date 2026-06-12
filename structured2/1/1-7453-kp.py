from itertools import *

s1 = "247 148 578 126 38 47 136 235".split()
s2 = "BA BH AH HF FG FD DC CG CE GE EA".split()


print(*range(1, 10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)