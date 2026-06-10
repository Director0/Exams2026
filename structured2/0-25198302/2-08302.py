print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = w and ((z or y) == (z and x))

                if f:
                    print(x, y, z, w, int(f))




print("\n-------------------\n")

print("x y z w F")

for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = w and ((z or y) == (z and x))

                if not f:
                    print(x, y, z, w, int(f))



