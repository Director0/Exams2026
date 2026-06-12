

rs = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if n % 3 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = n1 + f"{(n % 3)*3:b}"

    r = int(n1, 2)

    if 100 <= r <= 130 or 130 <= r <= 160:
        rs.append((n, r))


print(sorted(rs, key=lambda x:x[1]))