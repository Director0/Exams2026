def f(x, y):
    return (3 * x + y > a) and (y < x) and (x < 30)

for a in range(1, 2000):
    if any(f(x, y) for x in range(1, 2000) for y in range(1, 2000)) == 0:
        print(a)