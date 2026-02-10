def f(x, y):
    return (3 * x + y > 48) or (x > y) or (4 * x + y < a)

for a in range(0, 100):
    if all(f(x, y) for x in range(0, 150) for y in range(0, 150)) == False:
        print(a)