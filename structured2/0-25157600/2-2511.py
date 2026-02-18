print("d m r z F")

for d in 0, 1:
    for m in 0, 1:
        for r in 0, 1:
            for z in 0, 1:
                F = ((d and (not(m and z))) and (not (m == r))) and ((d == m) <= ((not r) or (z <= m)))

                if F == 1:
                    print(d, m, r, z, int(F))