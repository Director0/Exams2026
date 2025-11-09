def div(n):
    dvs = set()

    for p in range(2, round(n**0.5) + 1):
        if n % p == 0:
            dvs.add(p)
            dvs.add(n // p)

    return sorted(dvs)


cnt = 0

for n in range(7305679, 10**10):
    dvs = div(n)

    if len(dvs) == 0: continue
    p1 = min(dvs)
    dvs = div(n // p1)

    if len(dvs) == 0: continue
    p2 = min(dvs)
    dvs = div(n // (p1 * p2))

    if len(dvs) == 0: continue
    p3 = min(dvs)
    p4 = n // (p1 * p2 * p3)

    s = p1 + p2 + p3 + p4

    if len(div(p4)) == 4 and str(s) == str(s)[::-1]:
        print(n, s)