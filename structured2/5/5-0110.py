res = []

for n in range(0, 256):
    n1 = f"{n:b}".zfill(8)
    n1 = n1.replace("1", "*").replace("0", "1").replace("*", "0")

    if int(n1, 2) % 5 == 0:
        n1 = "100" + n1[3:]
    else:
        n1 = "101" + n1[3:]

    r = int(n1, 2)

    if r == 180:
        res.append([n, r])

print(res)
print(len(res))