
for n in range(100, 1000):
    n1 = [int(x) for x in str(n)]
    n2 = "".join(str(x) for x in sorted([(n1[0]**2 + n1[1]**2), (n1[1]**2 + n1[2]**2)], reverse=True))

    if n2 == "9010":
        print(n, n2)