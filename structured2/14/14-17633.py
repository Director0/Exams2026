def conv(num, n):
    res = ""

    while num > 0:
        res += str(num % n)
        num //= n

    return res[::-1]


for x in range(1, 2031):
    if conv(6**260 + 6**160 + 6**60 - x, 6).count("0") == 202:
        print(x)