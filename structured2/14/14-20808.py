rs = []

def conv(num, n):
    res = ""

    while num > 0:
        res += str(num % n)
        num //= n

    return res[::-1]


for x in range(1, 2031):
    rs.append((x, conv(7**170 + 7**100 - x, 7).count("0")))


print(sorted(rs, key=lambda x:x[1]))