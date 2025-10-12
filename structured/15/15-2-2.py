def f(x):
    return (not ((x % 12 == 0) and (x % 5))) or (x % a)


for a in range(1, 1000):
    if all(f(x) for x in range(1, 1000)) != 0:
        print(a)

