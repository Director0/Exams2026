alb = "0123456789ABCD"


def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

for x in range(1, 99):
    n1 = 7 * 100**6 + alb.index("A") * 100**5 + x * 100**4 + 0 * 100**3 + 1 * 100**2 + 2 * 100**1 + 3
    n2 = 1 * 100**5 + alb.index("B") * 100**4 + alb.index("A") * 100**3 + 6 * 100**2 + 4 * 100**1 + x
    n3 = x * 100**6 + 9 * 100**5 + 8 * 100**4 + 0 * 100**3 + 1 * 100**2 + 2 * 100**1 + alb.index("C")

    if (n1 - n2 + n3) % 21 == 0:
        print(x, conv(x, 6))