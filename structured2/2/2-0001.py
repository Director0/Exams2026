print("a b c d")

for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                F = c and (a or d) and (d <= b)

                if F == 1:
                    print(a, b, c, d)
