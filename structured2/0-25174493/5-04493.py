def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


res = []

for n in range(1, 1000):
    n1 = conv(n, 3)

    if n % 2 == 0:
        n1 = "2" + n1 + conv(int(n1[-1]) * 2, 3)
    else:
        n1 = conv(int(n1[0]) * 2, 3) + n1 + "2"

    r = int(n1, 3)

    if r > 100:
        res.append((n, r))


print(min(res, key=lambda x:x[1]))