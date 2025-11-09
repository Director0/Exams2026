def div(n):
    divs = set()

    for p in range(2, round(n ** 0.5) + 1):
        if n % p == 0:
            divs.add(p)
            divs.add(n // p)

    return sorted(divs)


cnt = 0

for n in range(1324728, 10**10):
    divs = div(n)

    if (len(divs) == 1 or len(divs) == 2) and str(divs[0]).count("5") == 1 and str(divs[-1]).count("5") == 1:
        print(n, max(divs))
        cnt += 1

        if cnt == 5:
            break