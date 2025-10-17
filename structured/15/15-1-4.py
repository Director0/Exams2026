def f(x, y):
    return (x >= 12) or (3 * x < y) or (x * y < a)

for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break