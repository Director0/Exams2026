from itertools import *

s1 = "45 345 256 127 123 37 46".split()
s2 = "AG AE ED DB BC BF FG GC CD".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)