
ls = []

for n in range(100, 201):
    n1 = f"{n:b}"

    if n1.count("1") % 2 == 0:
        n1 = n1 + "10"
    else:
        n1 = "11" + n1

    r1 = int(n1, 2)

    nn1 = f"{r1:b}"

    if nn1.count("1") % 2 == 0:
        nn1 = nn1 + "10"
    else:
        nn1 = "11" + nn1

    r = int(nn1, 2)

    if r % 2 == 0:
        ls.append((n, r))


print(ls)
print(len(ls))