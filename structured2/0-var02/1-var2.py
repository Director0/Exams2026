from itertools import *

s1 = "247 13567 26 15 24 238 128 67".split()
s2 = "AB AH BC FG GH CH CD DH DE EF FH".split()

print(* range(1,9))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)
