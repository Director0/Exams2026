

for p in range(10, 100):
    for x in range(0, p):
        for y in range(1, p):
            for z in range(1, p):
                for w in range(1, p):
                    if len([x, y, z, w]) == len(set([x, y, z, w])):
                        n1 = y * p**3 + 0 * p**2 + 7 * p**1 + x
                        n2 = w * p**3 + y * p**2 + 9 * p**1 + z
                        n3 = z * p**4 + x * p**3 + y * p**2 + x * p**1 + y

                        if n1 + n2 == n3:
                            print(p, x * p**3 + y * p**2 + z * p**1 + w)