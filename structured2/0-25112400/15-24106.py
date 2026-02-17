def f(x, y):
    return ((2 * x * y) > a) or (y < x) or (x < 15)


for a in range(1, 1000):
    if all(f(x,y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)