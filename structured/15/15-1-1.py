def f(x, y):
    return (x >= 8) or (a < (x * y)) or (y <= 7)

for a in range(1, 5000):
    if all(f(x, y) for x in range(1, 5000) for y in range(1, 5000)):
        print(a)