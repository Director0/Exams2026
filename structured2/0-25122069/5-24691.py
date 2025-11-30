res = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if n % 5 == 0:
        n1 = f"{5:b}" + n1
    else:
        n1 = n1 + n1[-1]

    r = int(n1, 2)

    if len(str(r)) == 3 and r % 2 == 0:
        res.append((n, r))

print(sorted(res))