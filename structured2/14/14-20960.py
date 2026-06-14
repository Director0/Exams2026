def conv(num, n):
    rs = ""

    while num != 0:
        rs += str(num % n)
        num //= n

    return rs[::-1]


m0 = 0

for x in range(1, 2005):
    n = conv(5**150 + 5**98 - x, 5)
    if n.count("0") >= m0:
        m0 = n.count("0")
        print(x, m0)