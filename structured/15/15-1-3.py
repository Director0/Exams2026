def f(x, y):
    return (2 * y > 5 * x) or (x * y < a) or (x >= 22)

for a in range(1, 2000):
    if all(f(x, y) for x in range(1, 2000) for y in range(1, 2000)):
        print(a)
        break