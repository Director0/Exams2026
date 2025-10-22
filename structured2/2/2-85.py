print("x y z w")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x == (not z)) <= ((x or w) == y)

                if F == 0:
                    print(x, y, z, w)


                    # 1 2 3 4
                    # x 0 y 0