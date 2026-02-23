def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]

res = []

for n in range(1, 1000):
    n1 = [x for x in conv(n, 3)]

    n1 = sorted(n1, reverse=True)
    n1 = n1 + [str(max([int(x) for x in n1]))]

    r = int("".join(n1), 3)

    if r < 1200:
        res.append((n, r))


print(sorted(res, key=lambda x:x[1]))
print(max(res, key=lambda x:x[1]))

