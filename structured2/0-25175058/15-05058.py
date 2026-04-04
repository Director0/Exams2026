def f(x, y):
    return ((x**2 > 60) or (not (x > a))) and ((not (y**2 > 90)) or (y > a))

cnt = 0

for a in range(1, 10000):
    if all(f(x, y) for x in range(1, 5000) for y in range(1, 5000)):
        cnt += 1
        print(a)


print(f"cnt: {cnt}")