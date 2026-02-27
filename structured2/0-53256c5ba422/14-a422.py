for x in range(401, 2000):
    n = 16 ** 560 + 16 ** 120 - x

    if hex(n)[2:].count("0") == 442:
        print(x)
        break