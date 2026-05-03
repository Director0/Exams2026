
res = []

for n in range(1, 256):
    n0 = f"{n:b}"
    n1 = ("0" * abs(8 - len(str(n0)))) + f"{n:b}"
    n2 = n1[::-1]

    r = int(n1, 2) - int(n2, 2)

    res.append((n, r))


print(sorted(res, key=lambda x:x[1]))