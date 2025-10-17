from itertools import *

p = set(range(2, 21, 2))
q = set(range(5, 51, 5))
d = p | q

def f(x, a):
    return ((x in a) <= (x in p)) and ((x in q) <= (x not in a))


for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            print(len(a), a)



# 8