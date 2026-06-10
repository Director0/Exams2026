
res = []

for n in range(1, 1000):
    n1 = f"{n:b}"

    if len(n1) % 2 == 0:
        n1 = n1 + "111"
    else:
        n1 = "11" + n1[2:] + "1"

    r = int(n1, 2)

    if r > 4000:
        res.append((n, r))



print(sorted(res))