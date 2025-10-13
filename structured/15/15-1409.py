from itertools import combinations

p = set(range(2, 21, 2))
q = set(range(3, 31, 3))
r = set(range(12, 61, 12))
d = p | q

def f(x, a):
    return (x not in a) <= (((x in p) and (x in q)) <= (x in r))

def an(n1):
    a1n = 1

    for x1 in n1:
        a1n = a1n * x1

    return a1n

ans = []

for n in range(len(d) + 1):
    for a in combinations(d, n):
        if all(f(x, a) for x in d):
            ans.append(an(a))
            print(an(a), a)


print("min ", min(ans))