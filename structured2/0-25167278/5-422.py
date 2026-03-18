def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


res = []

for n in range(1, 1000):
    n1 = conv(n, 6)

    n1 = int(str(n1) + str(n1)[-1], 6)
    n1 = conv(n1, 2)

    r = int(str(n1) + str(n1)[-1], 2)

    if r < 344:
        res.append((n, r))


print(sorted(res, key=lambda x:x[1], reverse=True))

