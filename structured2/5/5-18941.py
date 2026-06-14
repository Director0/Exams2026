for n in range(1000, 10000):
    n0 = [int(x) for x in str(n)]
    n1 = "".join([str(x) for x in sorted(sorted([n0[0] * n0[1], n0[0] * n0[2], n0[0] * n0[3]], reverse=True)[:2])])

    if n1 == "5472":
        print(n, n1)