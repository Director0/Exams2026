from itertools import *

s1 = "346 348 12 127 678 15 458 257".split()
s2 = "DC DB DA AH AE EG GH GF FC CB".split()

print(* range(1,9))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)
