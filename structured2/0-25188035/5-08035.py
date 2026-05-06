
res = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if n % 2 == 0:
        n1 = "1" + n1 + "0"
    else:
        n1 = "11" + n1 + "11"

    r = int(n1, 2)

    if r > 225:
        res.append((n, r))


print(sorted(res, key=lambda x:x[1]))