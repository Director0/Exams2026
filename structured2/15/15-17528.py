def f(x, a1, a2):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2

    return p <= ((q and (not a)) <= (not p))

minl = 10 ** 10

for a1 in range(15, 70):
    for a2 in range(a1, 70):
        if all(f(x, a1, a2) for x in range(15, 70)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)