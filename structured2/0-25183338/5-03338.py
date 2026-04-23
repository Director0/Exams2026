res = []


for n in range(1, 5000):
    n1 = f"{n:b}"

    if n % 2 == 0:
        n1 = n1 + "100"
    else:
        n1 = n1 + "011"

    r = int(n1, 2)

    if r > 300:
        res.append((n, r))


print(sorted(res))