def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


res = []

for n in range(1, 1000):
    n1 = conv(n, 3)

    if n % 3 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = n1 + conv(sum([int(x) for x in n1]), 3)

    r = int(n1, 3)

    if r > 520 and r % 2 != 0:
        res.append((n, r))


print(sorted(res, key=lambda x:x[1]))