def f(x):
    return ((x % a == 0) and (x % 24 == 0)) and ((not (x % 16 == 0)) <= (not (x % a == 0)))

for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)