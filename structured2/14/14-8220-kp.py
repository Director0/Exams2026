for x in range(0, 9):
    n1 = 1 * int(f"9{x}87")**1 + 3
    n2 = 1 * 100**2 + x * 100**1 + 9

    if (n1 + n2) % 99 == 0:
        print((n1 + n2) / 99)