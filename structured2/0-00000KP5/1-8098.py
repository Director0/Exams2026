from itertools import *

s1 = "457 567 45 136 123 247 126".split()
s2 = "".split()

print(* range(1,10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)