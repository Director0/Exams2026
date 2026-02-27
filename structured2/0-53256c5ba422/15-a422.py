def f(x, y):
    return ( (-(x-2)**2 + 3) < y) or (((x-1)**2 + y**2) < 7) or ((5*x + a) > y)


for a in range(0, 1000):
    if all(f(x, y) for x in range(0, 100) for y in range(0 ,100)):
        print(a)