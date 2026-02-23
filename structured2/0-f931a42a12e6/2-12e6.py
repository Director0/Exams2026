print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                F = (y == (not w)) <= (not(w and (x == (x or (w <= z)))))

                if F == 0:
                    print(x, y, z, w, int(F))