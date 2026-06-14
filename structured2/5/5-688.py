res = []

for n in range(0, 110):
    n1 = f"{n:b}".zfill(8)
    n1 = n1[:2] + n1[-2:]

    r = int(n1, 2)

    if r == 7:
        res.append((n, r))


print(max(res))
