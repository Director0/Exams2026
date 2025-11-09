res = []

for m in range(2, 100, 2):
    for n in range(1, 100, 2):
        if 200000000 <= (2**m * 3**n) <= 400000000:
            res.append(2**m * 3**n)


print(*sorted(res))
