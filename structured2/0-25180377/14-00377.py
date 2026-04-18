def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


for x in range(1, 10000):
    if int("100", 5) + x == int("200", 4):
        print(x, conv(x, 7))