res = []

for n in range(33, 1000):
    n1 = f"{n:b}"

    if n % 2 != 0:
        n1 = "1" + n1[:-2] + "10"
    else:
        n1 = "10" + n1[2:] + "1"

    r = int(n1, 2)

    res.append((n, r))


print(res)
print(min(res, key=lambda x:x[1]))