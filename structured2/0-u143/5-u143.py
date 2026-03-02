def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


res = []


for n in range(1, 10000):
    n1 = conv(n, 4)

    if n % 4 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = n1 + conv((n % 4) * 2, 4)

    r = int(n1, 4)

    if r < 479:
        res.append((n, r))


print(res)
print(max(res))