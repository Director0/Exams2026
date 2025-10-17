alb = "abcdefghijklmnopqrstuvwxyz"

for x in range(0, 42):
    x1 = 19 * 42 ** 4 + 5 * 42 ** 3 + 6 * 42 ** 2 + 9 * 42 ** 1 + x
    x2 = 1 * 42 ** 3 + x * 42 ** 2 + (10 + (alb.index("i"))) * 42 ** 1 + 10
    # x2 = 1 * 42 ** 3 + x * 42 ** 2 + 18 * 42 ** 1 + 10

    if (x1 + x2) % 155 == 0:
        print(x, (x1 + x2) // 155)

