def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

res1 = []

for n in range(1, 1000):
    n4 = conv(n, 4)

    if n % 4 == 0:
        n4 = n4 + n4[0:1]
    else:
        n4 = n4 + conv(((n % 4)*4), 4)

    r = int(n4, 4)

    if r > 291:
        res1.append([r, n])

print(min(res1))
