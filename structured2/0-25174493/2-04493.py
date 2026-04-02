print("x y z F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            F = x <= y and z

            if F == 0:
                print(x, y, z, int(F))