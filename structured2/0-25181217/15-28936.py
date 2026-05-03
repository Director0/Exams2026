def f(x, y):
    return (x * y < a) or (5*x < y) or (486 <= x)


for a in range(0, 10000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)