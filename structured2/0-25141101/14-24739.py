alb = "0123456789ABCDEFGHIJK"


for x in range(0, 21):
    x1 = alb.index("E") * 21**4 + alb.index("F") * 21**3 + x * 21**2 + 6 * 21**1 + 7
    x2 = 3 * 21**4 + alb.index("H") * 21**3 + x * 21**2 + 4 * 21**1 + alb.index("C")

    if (x1 + x2) % 20 == 0:
        print(x)
        print((x1 + x2) // 7)