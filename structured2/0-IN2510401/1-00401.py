from itertools import *

s1 = "357 347 12567 26 13 34 123".split()
s2 = "AB AD AF FD FG GD GE ED DC CB".split()

print(* range(1,10))

for p in permutations("ABCDEFG"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x, y in s2):
        print(*p)