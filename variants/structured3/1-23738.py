from itertools import *

s1 = "258 17 56 68 138 347 26 145 ".split()
s2 = "FH HD HB BC CA CG GE GA DA".split()

print(* range(1,9))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)

#52