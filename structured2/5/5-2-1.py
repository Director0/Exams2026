
for n in range(1, 1000):
    n1 = bin(n)[2:]

    if n % 2 == 0:
        n1 = n1 + "0" * n1.count("0")
    else:
        n1 = "1" * n1.count("1") + n1

    r = int(n1, 2)

    if r > 2000:
        print(n, r)
        break