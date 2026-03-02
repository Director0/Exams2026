def f(x, a):
    return ((x % a == 0) and (x % 8 == 0)) <= ((not((x % 8 == 0))) or (x % 240 == 0))


for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 10000000)):
        print(a)


if all(f(x, 240) for x in range(1, 10101)):
    print("ok")