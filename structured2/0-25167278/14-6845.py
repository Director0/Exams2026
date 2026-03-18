alb = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(len(alb))

for p in range(37):
    alb1 = alb[1:p]

    for x in alb1:
        for y in alb1:
            n1 = 1 * p**3 + (alb1.index(x) + 1) * p**2 + 7 * p**1 + 7
            n2 = (alb1.index(x) + 1) * p**3 + (alb1.index(x) + 1) * p**2 + 7 * p**1 + 7

            n3 = (alb1.index(y) + 1) * p**3 + 0 * p**2 + (alb1.index(y) + 1) * p**1 + (alb1.index(y) + 1)

            if n1 + n2 == n3:
                print(p, x, y)
                nx = (alb1.index(y) + 1) * p**3 + (alb1.index(x) + 1) * p**2 + (alb1.index(y) + 1) * p**1 + (alb1.index(x) + 1)
                print(nx)

