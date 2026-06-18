

for p in range(10, 1000):
    for x in range(1, p):
        for y in range(1, p):
            n1 = x * p**3 + x * p**2 + x * p**1 + 8
            n2 = 4 * p**3 + 3 * p**2 + x * p**1 + 9
            n3 = y * p**3 + y * p**2 + 0 * p**1 + 4

            if n1 + n2 == n3:
                print(p, y * p**2 + y * p**1 + x)