from itertools import permutations

s1 = "367 345 125 26 23 147 16".split()
s2 = "".split()

print(* range(1, 9))

for p in permutations(""):
    if all(str(p.index(x) + 1) in s1[p.index(y)] for x, y in s2):
        print(*p)