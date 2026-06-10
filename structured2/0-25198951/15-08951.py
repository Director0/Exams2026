p = set(x for x in range(2, 22, 2))
q = set(x for x in range(3, 33, 3))
r = set(sorted(set(x for x in range(12, 72, 12))))
d = p | q | r

res = []

def f(x, a):
    return (x not in a) <= (((x in p) and (x in q)) <= (x in r))


from itertools import combinations

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            r1 = 1
            for b in a:
                r1 *= b
                res.append(r1)
            print(len(a), a, r1)


print(min(res))