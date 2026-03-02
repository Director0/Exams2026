print("x y z F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = (y or x) <= (z == y)

            if F == 0:
                print(x, y, z, int(F))