p = set(range(1, 12, 2))
q = set(range(3, 13, 3))
d = p | q

def f(x, a):
    return (x in p) <= (not(x in q)) or (x in a)


from itertools import combinations

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            print(len(a), a, sum(a))