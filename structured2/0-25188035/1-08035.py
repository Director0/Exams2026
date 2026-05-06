from itertools import *

s1 = "24 135 256 157 234 37 46".split()
s2 = "AD AF DE DB EF EG GF GC CB".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)