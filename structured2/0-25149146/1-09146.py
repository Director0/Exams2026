from itertools import *

s1 = "456 37 25 16 137 147 256".split()
s2 = "AE AG GB BE BF FC FD DC CE".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)