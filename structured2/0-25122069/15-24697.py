def f(x, a1, a2):
    p = 15 <= x <= 40
    q = 21 <= x <= 63
    a = a1 <= x <= a2

    return (x in p) <= ((not( not(x in q) or (x in a) )) <= (not(x in p)))

minl = 10 ** 10

for a1 in range(13, 60):
    for a2 in range(a1, 60):
        if all(f(x, a1, a2) for x in range(13, 60)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)