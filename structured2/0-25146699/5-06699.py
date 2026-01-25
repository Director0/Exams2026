
for n in range(128, 256):
    n1 = f"{n:b}"

    n1 = n1.replace("1", "*").replace("0", "1").replace("*", "0")

    r1 = int(n1, 2)

    r = n - r1

    if r == 105:
        print(n, n1, r1, r)