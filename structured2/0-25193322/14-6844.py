for p in range(3, 40):
    for x in range(1, p):
        for y in range(1, p):
            n1 = 5 * p ** 3 + x * p ** 2 + 8 * p ** 1 + 3
            n2 = x * p ** 3 + 9 * p ** 2 + x * p ** 1 + 9
            n3 = y * p ** 3 + 2 * p ** 2 + 0 * p ** 1 + y

            if n1 + n2 == n3:
                print(x, y, p)


x = 6
y = 12
p = 14

print(x * p ** 3 + y * p ** 2 + y * p ** 1 + x)