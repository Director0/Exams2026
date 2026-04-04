alb = "0123456789abcdefghijklmnopqrstuvwxyz"

for p in range(11, 100):
    for x in range(1, 500_000):
        x1 = 2 * p**3 + 9 * p**2 + alb.index("a") * p**1 + 1
        x2 = 4 * p**4 + 7 * p**3 + 7 * p**2 + 7 * p**1 + 1
        x3 = 1 * p**2 + 2 * p**1 + alb.index("a")

        if (x1 + x2 + x3) == 1000000 + x:
            print(p)