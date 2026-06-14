def conv(num, n):
    rs = ""

    while num > 0:
        rs += str(num % n)
        num //= n

    return rs[::-1]


rs = []

for n in range(1, 1000):
    n1 = conv(n, 12)

    if n % 3 == 0:
        n1 = "1" + n1 + "B"
    else:
        n1 = "2" + n1 + "0"

    r = int(n1, 12)

    if r < 1996:
        rs.append((n, r))


print(sorted(rs))