from itertools import *

s1 = "346 348 12 127 678 15 458 257".split()
s2 = "AD AH AE EG GH GF FC CB BH BD DC".split()

print(* range(1,10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)