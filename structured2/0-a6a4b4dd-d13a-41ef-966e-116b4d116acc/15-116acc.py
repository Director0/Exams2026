def f(x, a1, a2):
    b = 101 <= x <= 143
    c = 144 <= x <= 199
    a = a1 <= x <= a2

    return a <= (b or c)


minl = 10 ** 20

for a1 in range(101, 210):
    for a2 in range(a1, 210):
        if all(f(x, a1, a2) for x in range(101, 210)):
            if (a2 - a1) < minl:
                minl, m1, m2 = a2 - a1, a1, a2


print(minl, m1, m2)