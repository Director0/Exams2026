
rs = []

for n in range(1, 5000):
    n1 = f"{n:b}"

    if n1.count("1") % 3 == 0:
        n1 = n1 + f"{(n1.count("1") % 5):b}"
    else:
        n1 = "1" + n1 + "10"

    r = int(n1, 2)

    if r > 89:
        rs.append((n, r))


print(sorted(rs, key=lambda x:x[1])[-1])