def conv(num, n):
    res = ""

    while num != 0:
        res += str(num % n)
        num //= n

    return res[::-1]


rs = []

for n in range(1, 3000):
    n1 = conv(n, 7)

    if n1.count("2") % 2 == 0:
        n1 = "555" + n1
    else:
        n1 = "1" + n1

    r = int(n1, 7)

    if r <= 3799:
        rs.append((n, r))



print(sorted(rs))