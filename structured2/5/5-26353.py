rs = []

for n in range(100_000, 1_000_000):
    n1 = [int(x) for x in str(n)]
    n2 = [int(x) for x in str(n) if x != "0"]
    r1 = 1

    b1 = sum(n1) - max(n1) - max(n1)

    for a in n2:
        r1 *= a

    b2 = r1 - 2 * sum(n1)

    r = "".join(str(x) for x in sorted([b1, b2], reverse=True))

    if r == "26714":
        print(n, r)