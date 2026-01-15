#print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = x and (w == (z == y and w))

                if F == 1:
                    print(y, w, x, z, int(F))