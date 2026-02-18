def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


for n in range(1, 1000):
    n1 = conv(n, 3)

    n1 = n1.replace("2", "*").replace("0", "2").replace("*", "0")

    r1 = int(n1, 3)
    r = abs(n - r1)

    if r == 378:
        print(n, r)