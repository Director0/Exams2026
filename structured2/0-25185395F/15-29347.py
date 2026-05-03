def f(x, a1, a2):
    b = 22 <= x <= 40
    c = 32 <= x <= 50
    a = a1 <= x <= a2

    return (not a) <= (b == c)


for a1 in range(22, 2000):
    for a2 in range(a1, 500):
        if all(f(x, a1, a2) for x in range(-1000, 1000)):
            print(a2 - a1, a1, a2)