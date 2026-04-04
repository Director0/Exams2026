from itertools import *

s1 = "457 567 45 136 123 247 126".split()
s2 = "AB AD AF FD FE EC EG GB BC CD ".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)