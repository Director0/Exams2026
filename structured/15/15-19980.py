def f(x, a1, a2):
    p = 52 <= x <= 105
    q = 0 <= x <= 53
    a = a1 <= x <= a2

    return ((not p) and (not q) and (not a)) <= (x ** 2 > 303601)


minl = 10 ** 10

for a1 in range(0, 1000):
    for a2 in range(a1, 1000):
        if all(f(x, a1, a2) for x in range(0, 1000)):
            if a2 - a1 < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)