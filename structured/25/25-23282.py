def div(n):
    dvs = set()

    for p in range(2, round(n**0.5), + 1):
        if n % p == 0:
            dvs.add(p)
            dvs.add(n // p)

    return sorted(dvs)


cnt = 0

for n in range(5400001, 10**10):
    dvs = div(n)
    dvs1 = [x for x in dvs if len(div(x)) == 0]
    ms = max(dvs1) + min(dvs1) if len(dvs1) > 0 else 0

    if ms > 60000 and str(ms) == str(ms)[::-1]:
        print(n, ms)
        cnt += 1

        if cnt == 5:
            break