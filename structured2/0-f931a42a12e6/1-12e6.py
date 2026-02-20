from itertools import *

s1 = "56 4678 4678 2357 14 1238 2348 2367".split()
s2 = "AD AG AH AB BC CF FH FE FD DE EG EH DG".split()

print(* range(1,10))

for p in permutations("ABCDEFGH"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)