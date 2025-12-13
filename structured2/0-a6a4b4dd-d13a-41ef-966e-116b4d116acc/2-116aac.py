print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:

                F = ((1 == w) == (not((w and x) or y))) <= z

                print(x, y, z, w, int(F))