# N2 UNSOLVED. resolve bruh 1:17:14 / task 6

print("x y z w F")

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                F = ((z <= y) == (w <= x)) or (x and z)

                if F == 0:
                    print(x, y, z, w, int(F))
