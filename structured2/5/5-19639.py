
rs = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if n1.count("0") % 2 == 0:
        n1 = "1" + n1 + "1"
    else:
        n1 = "10" + n1

    r = int(n1, 2)

    if r < 100:
        rs.append((n, r))


print(sorted(rs, key=lambda x:x[1]))