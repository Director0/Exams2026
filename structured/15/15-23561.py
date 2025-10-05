def f(x):
    return (x % 128 == 0) <= ((not (x % a == 0)) <= (not (x % 80 == 0)))

for a in range(1, 20000):
    if all(f(x) for x in range(1, 20000)):
        print(a)