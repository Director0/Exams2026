from itertools import *

p = set(range(1, 11))
q = {2, 4, 8, 10}
d = p | q

def f(x, a):
    return ((x in q) <= (x in a)) and ((x in a) <= (x in p))

cnt = 0

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            print(a)
            cnt += 1

print("cnt: ", cnt)