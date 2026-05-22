rs = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if n1.count("1") % 2 == 0:
        n1 = "10" + n1[2:] + "0"
    else:
        n1 = "11" + n1[2:] + "1"

    r = int(n1, 2)

    if r <= 19:
        rs.append((n, r))


print(sorted(rs, reverse=True))
print(max(rs)[0])