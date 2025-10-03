from itertools import *

s1 = "23 168 158 578 347 27 456 234".split()
s2 = "DE DF DB BH BG HE EA AF FC CG GH".split()

print(* range(1,9))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)
