

p = set(range(2, 22, 2))
q = set(range(3, 33, 3))
d = p | q

def f(x, a):
    return ((x in a) <= (x in p)) and ((x not in q) <= (x not in a))


# for x in range(-1000, 1000):

from itertools import combinations

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in range(-100, 100)):
            print(len(a), a)