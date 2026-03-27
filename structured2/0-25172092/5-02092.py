
res = []

for n in range(4, 1000):
    n1 = f"{n:b}"

    if n % 3 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = n1 + f"{((n % 3) * 3):b}"

    r = int(n1, 2)

    if r > 76:
        res.append((n, r))


print(sorted(res))