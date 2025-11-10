def conv(n, st):
    res = ""

    while n != 0:
        res += str(n % st)
        n //= st

    return res[::-1]


res = []

for n in range(1, 1000):
    n1 = conv(n, 3)

    if n % 3 == 0:
        n1 = "1" + n1 + "02"
    else:
        n1 = n1 + conv(((n % 3) * 4), 3)

    r = int(n1, 3)

    if r < 100:
        print(n, r)
        res.append((n, r))


print(max(res))