def f(x, a1, a2):
    p = 10 <= x <= 150
    q = 160 <= x <= 250
    r = 240 <= x <= 300
    a = a1 <= x <= a2

    return (q <= p) or ((not a) <= r)


minl = 10 ** 10
for a1 in range(7, 310):
    for a2 in range(a1, 310):
        if all(f(x, a1, a2) for x in range(7, 310)):
            if a2 - a1 < minl:
                minl, m1, m2 = a2 - a1, a1, a2

print(minl, m1, m2)



