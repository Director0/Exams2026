def conv(num, n):
    rs = ""

    while num != 0:
        rs +=str(num % n)
        num //= n

    return rs[::-1]


rs = []

for n in range(1, 1000):
    n1 = conv(n, 4)

    if n % 3 == 0:
        n1 = n1[-1] + n1[1:-1] + n1[0] + "1"
    else:
        n1 = n1 + conv((n % 3), 4)

    r = int(n1, 4)

    if r <= 340:
        rs.append((n, r))


print(sorted(rs, key=lambda x:x[1]))