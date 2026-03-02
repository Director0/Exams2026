alb = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for x in range(0, 24):
    n1 = alb.index("F") * 24**4 + alb.index("E") * 24**3 + x * 24**2 + 7 * 24**1 + 6
    n2 = alb.index("C") * 24**4 + 4 * 24**3 + x * 24**2 + 3 * 24**1 + alb.index("H")

    n3 = 1 * 24**5 + 3 * 24**4 + alb.index("J") * 24**3 + alb.index("E") * 24**2 + alb.index("A") * 24**1 + alb.index("N")

    if n1 + n2 == n3:
        print(x)


x = 19
nx = alb.index("A") * 33**4 + x * 33**3 + alb.index("A") * 33**2 + x * 33**1 + alb.index("A")
print(nx)