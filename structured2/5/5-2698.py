
rs = []

for n in range(1, 10000):
    n1 = f"{n:b}"[::-1]

    if n1[0] == "0":
        n1 = "1" + n1

    n1 = n1 + f"{n:b}"

    R = int(n1, 2)

    if R <= 6000:
        rs.append((n, R))

print(max(rs))
print(rs)