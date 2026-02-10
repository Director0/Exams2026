from itertools import *

s1= "47 57 45 136 236 457 126".split()
s2 = "AG AE EC ED DB BC CG BF FG".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)