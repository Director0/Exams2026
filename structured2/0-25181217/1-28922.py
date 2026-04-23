from itertools import *

s1 = "47 458 67 125 146 35 138 27".split()
s2 = "AB AH HF FD FE EG GB GC BC CD".split()

print(* range(1,10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)