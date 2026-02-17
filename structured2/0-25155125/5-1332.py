for n in range(1, 1000):
    n1 = f"{n:b}"

    n2 = n1[0] + n1[1:].replace("1", "*").replace("0", "1").replace("*", "0")

    r = int(n2, 2) + n

    print(n, r)