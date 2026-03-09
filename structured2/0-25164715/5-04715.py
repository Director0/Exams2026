res = []

for n in range(1, 10000000):
    n1 = n

    if n1 % 3 == 0:
        n1 = n1 // 3
    else:
        n1 = n1 - 1

    if n1 % 5 == 0:
        n1 = n1 // 5
    else:
        n1 = n1 - 1

    if n1 % 11 == 0:
        n1 = n1 // 11
    else:
        n1 = n1 - 1

    if n1 == 8:
        res.append((n, n1))


print(res)
print(len(res))