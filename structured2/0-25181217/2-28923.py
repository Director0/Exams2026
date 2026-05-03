print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (x and (not z) and (not w)) or (x and (not z) and y)

                if F == 1:
                    print(x, y, z, w, int(F))



