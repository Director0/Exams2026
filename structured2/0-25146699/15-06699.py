def f(x, a1, a2):
    b = 25 <= x <= 40
    c = 12 <= x <= 33
    a = a1 <= x <= a2

    return (b <= a) and ((not c) or a)


minl = 10**10

for a1 in range(25, 120):
    for a2 in range(a1, 120):
        if all(f(x, a1, a2) for x in range(25, 41)) == 1:
            if (a2 - a1) < minl:
                minl = a2 - a1


print(minl)