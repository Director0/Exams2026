def conv(num, n):
    rs = ""

    while num != 0:
        rs += str(num % n)
        num //= n

    return rs[::-1]

rs = []

for n in range(1, 1000):
    n1 = conv(n, 3)

    if n % 3 == 0:
        n1 = "1" + n1 + "02"
    else:
        n1 = n1 + conv((n % 3) * 4, 3)

    r = int(n1, 3)

    if r < 199:
        rs.append((n, r))


print(sorted(rs))