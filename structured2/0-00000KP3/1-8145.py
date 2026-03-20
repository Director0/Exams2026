from itertools import *

s1 = "234 136 12 157 467 25 45".split()
s2 = "AE AD DF DB BF FG GE GC CE".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)