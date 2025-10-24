
rs = []

for n in range(1, 10000):
    n0 = f"{n:b}"
    n1 = n0[0] + n0[1:].replace("1", "x").replace("0", "1").replace("x", "0")
    # print(f"n: {n}, nbin: {n0} , rbin: {n1}")

    r = int(n1, 2)
    r = n + r

    rs.append((n, r))

print(sorted(rs))
for rs1 in sorted(rs):
    if rs1[0] % 2 != 0 and rs1[1] > 99:
        print(rs1)
        break