def f(x, y):
    return (3*x + 4*y < 814625) or (y < x - 1222) or (y > a)


for a in range(1, 1000):
    if all(f(x,y) for x in range(1, 10000) for y in range(1, 10000)):
        print(a)