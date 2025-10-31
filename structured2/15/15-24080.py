def f(x, a1, a2):
    c = 25 <= x <= 64
    t = 50 <= x <= 120
    a = a1 <= x <= a2

    return not ((c <= a) <= t)


minl = 10 ** 20


for a1 in range(25, 150):
    for a2 in range(a1, 150):
        if any(f(x, a1, a2) for x in range(25, 150)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)