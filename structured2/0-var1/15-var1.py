def f(x, y):
    return ((x < 6) <= (x**2 < a)) and ((y**2 <= a) <= (y <= 6))

cnt = 0
for a in range(1, 1000):
    if all(f(x, y) for x in range(0, 1000) for y in range(0, 1000)):
        print(a)
        cnt += 1

print(cnt)