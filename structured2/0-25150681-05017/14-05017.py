def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

for s in range(2, 31):
    if len(conv(50, s)) == 2:
        print(conv(50, s), s)