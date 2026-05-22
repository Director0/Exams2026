print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z == (not x)) <= ((w <= (not y)) and (y <= x))

                if f == 1:
                    print(x, y, z, w, int(f))