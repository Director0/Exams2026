res = []

def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


for n in range(1, 1000):
    n1 = conv(n, 4)

    if n % 4 == 0:
        n1 = n1 + n1[-2:]
    else:
        n1 = conv((n % 4) * 2, 4) + n1

    r = int(n1, 4)

    if r > 280:
        res.append((n, r))

print(res)
print(min(res, key=lambda x:x[1]))