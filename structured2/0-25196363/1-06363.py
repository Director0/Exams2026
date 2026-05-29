from itertools import *

s1 = "37 367 125 56 34 247 126".split()
s2 = "AB AD DE EB EG GC CF FB FA".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)