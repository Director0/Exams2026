def f(x, y):
    return ((x < a) <= (x * x <= 169)) and ((y * y < 16) <= (y <= a))


cnt = 0
for a in range(1, 1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        cnt += 1

print("cnt: ", cnt)