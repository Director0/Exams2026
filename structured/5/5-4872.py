res = [1, 2]

for n in range(10, 1000):
    res1 = res + list(int(x) for x in str(n))

    p1 = 1
    p2 = 1

    for i in res1:
        if i != 0 and i % 2 == 0:
            p1 *= i
        else:
            p2 *= i

    r1 = abs(p1 - p2)

    if r1 == 29:
        print(n, r1)
        break


