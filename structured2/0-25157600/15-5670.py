def f(x):
    return (x + a >= 160) or ((x % 7 == 0) <= (not(x + (-17) > 0)))

for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)):
        print(a)