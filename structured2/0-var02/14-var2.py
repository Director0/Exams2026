def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

for x in range(1, 2301):
    n1 = 7 ** 350 + 7 ** 150 - x

    if conv(n1, 7).count("0") == 200:
        print(x)