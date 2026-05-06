def f(x, a1, a2):
    p = 25 <= x <= 64
    q = 40 <= x <= 115
    a = a1 <= x <= a2

    return p <= ((q and (not a)) <= (not p))


for a1 in range(25, 1000):
    for a2 in range(a1, 1000):
        if all(f(x, a1, a2) for x in range(-100000, 100000)):
            print(a2 - a1, a1, a2)