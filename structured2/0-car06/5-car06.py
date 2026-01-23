res = []

for n in range(1, 5000):
    n1 = f"{n:b}"

    if n % 3 == 0:
        n1 = n1 + n1[-3:]
    else:
        n1 = n1 + str(f"{(n % 3) * 3:b}")

    r = int(n1, 2)

    if r < 130:
        res.append([n, r])

print(res)
print(max(res))