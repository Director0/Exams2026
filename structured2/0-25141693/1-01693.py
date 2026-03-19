from itertools import *

s1 = "478 38 256 15 34 37 168 127".split()
s2 = "AH AG GD DE EF FH FB HB BC CG".split()

print(* range(1,10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)