from itertools import *

s1 = "26 147 456 236 37 134 25".split()
s2 = "AG AB AD GB GF BC DC DE EF".split()

print(* range(1,9))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)
