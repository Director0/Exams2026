def f(x, a1, a2):
    b = 1 <= x <= 9999
    c = 3648 <= x <= 6287
    a = a1 <= x <= a2

    return (b == c) or a or (x > 4200)

minl = 10**20
m1, m2 = None, None

for a1 in range(1, 1000):
    for a2 in range(a1, 1000):
        if all(f(x, a1, a2) for x in range(1, 10000)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)