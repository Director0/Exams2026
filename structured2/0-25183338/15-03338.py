def f(x, y, z):
    return (150 != y + 2*x + 2*x) or (a < x) or (a < y) or (a < z)


for a in range(0, 10000):
    if all(f(x, y, z) for x in range(1, 100) for y in range(1, 100) for z in range(1, 100)):
        print(a)