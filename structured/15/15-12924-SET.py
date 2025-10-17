p = set(range(2, 21, 2))
q = set(range(3, 31, 3))
d = p | q

def f(x, a):
    return ((x in a) <= (x in p)) and ((x not in q) <= (x not in a))

from itertools import combinations

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            print(len(a), a)



