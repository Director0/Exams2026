print("x y z w I J")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F1 = (w == x) and (y <= z)
                F2 = (w <= x) <= (y == z)

                if F1 == 1 and F2 == 1:
                    print(x, y, z, w, int(F1), int(F2))