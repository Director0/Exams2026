
res = []

for n in range(10**8, 10**9):
    n1 = f"{sum([int(x) for x in str(n)]):b}"

    if n1.count("1") % 2 == 0:
        n1 = "1" + n1 + "00"
    else:
        n1 = "10" + n1 + "1"

    r = int(n1, 2)

    if r == 21:
        res.append((n, r))
        print((n, r))


print(res)
print(len(res))