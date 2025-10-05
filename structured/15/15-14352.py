def f(x):
    b = 120 <= x <= 180

    return (x % a == 0) or ((b) <= ((not(x % 16 == 0)) or (x + a <= 204)))

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)