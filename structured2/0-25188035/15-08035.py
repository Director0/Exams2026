def f(x, a1, a2):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2

    return p <= ((q and (not a)) <= (not p))


res = set()

for a1 in range(0, 100):
    for a2 in range(a1 + 1, 100):
        if all(f(x, a1, a2) for x in range(-100000, 100000)):
            res.add(a2 - a1)
            print(a2 - a1, a1, a2)


print(min(res))