def f(x):
    return (x & a != 0) <= ((x & 168 == 0) <= (x & 69 != 0))

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)