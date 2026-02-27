print("x y u w")

for x in 0, 1:
    for y in 0, 1:
        for u in 0, 1:
            for w in 0, 1:
                F = (x <= w) <= (u <= y)

                if F == 0:
                    print(x, y, u, w, int(F))