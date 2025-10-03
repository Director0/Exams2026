print("a b c F")

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            F = (a <= b) and (a and b <= (not c))

            if F:
                print(a, b, c, int(F))