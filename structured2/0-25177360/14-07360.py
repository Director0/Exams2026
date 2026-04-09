for x in range(1, 2005 + 1):
    x1 = 4 ** 163 * 5 + 12**62 - x

    c1 = 0
    c4 = 0

    while x1 != 0:
        if x1 % 5 == 1:
            c1 += 1
        elif x1 % 5 == 4:
            c4 += 1

        x1 //= 5

    if c1 < c4:
        print(x)

