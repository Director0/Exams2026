res = []
r1 = set()

for n in range(0, 256 + 1):
    n1 = f"{n:b}"

    if n % 2 == 0:
        n1 = "11" + n1 + "0"
    else:
        n1 = "1" + n1 + "00"

    r = int(n1, 2)

    res.append(r)

print(sorted(res))

for x in res:
    if res.count(x) > 1:
        r1.add(x)

print("\n", sorted(r1))
print("\n", len(r1))
