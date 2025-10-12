def f(x, a1, a2):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <= x <= a2

    return p <= ((q and (not a)) <= (not p))

minl = 10 ** 10

for a1 in range(20, 120):
    for a2 in range(a1, 120):
        if all(f(x, a1, a2) for x in range(20, 120)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2

print(minl, m1, m2)