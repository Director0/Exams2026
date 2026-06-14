
rs = []

for n in range(1, 13):
    n1 = f"{n:b}"

    if n % 2 == 0:
        n1 = "10" + n1
    else:
        n1 = "1" + n1 + "01"

    r = int(n1, 2)

    rs.append((n, r))


print(sorted(rs, key=lambda x:x[1]))