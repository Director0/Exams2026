def conv(num, n):
    rs = ""

    while num != 0:
        rs += str(num % n)
        num //= n

    return rs[::-1]


rs = []

for n in range(1, 1000):
    n1 = conv(n, 4)

    if n1[0] == "3":
        n1 = "21" + n1.replace("3", "*").replace("1", "3").replace("*", "1")
    else:
        n1 = "1" + n1[1:] + "12"

    r = int(n1, 4)

    if r < 598:
        rs.append((n, r))



print(sorted(rs, key=lambda x:x[1], reverse=True))