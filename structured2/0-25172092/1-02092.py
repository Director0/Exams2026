from itertools import *

s1 = "23567 145 146 23 127 137 156".split()
s2 = "AE AD AB BD BC CD CF FD FG GE ED".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)