res = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    n1 = n1 + str(n1.count("1") % 2)
    n1 = n1 + str(n1.count("1") % 2)

    r = int(n1, 2)

    if r > 253:
        res.append((n, r))


print(min(res))