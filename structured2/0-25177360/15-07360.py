def f(x, a1, a2):
    p = 257 <= x <= 1000
    q = 5 <= x <= 100
    r = 99 <= x <= 258
    a = a1 <= x <= a2

    return (a <= r) and ((not(x <= p)) <= q)


for a1 in range(0, 2000):
    for a2 in range(a1, 2000):
        if all(f(x, a1, a2) for x in range(0, 1000)):
            print(a2 - a1, a1, a2)
