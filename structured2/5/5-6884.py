rs = []

for n in range(1, 10000):
    n1 = f"{n:b}"


    if n % 2 == 0:
        n2 = "1" + n1 + "0"

    else:
        n2 = "11" + n1 + "11"

    r = int(n2, 2)

    if r > 225:
        print(r)
        rs.append(r)


print(min(rs))