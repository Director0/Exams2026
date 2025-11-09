def div(n):
    divs = set()

    for p in range(1, round(n ** 0.5) + 1):
        if n % p == 0:
            divs.add(p)
            divs.add(n // p)

    return sorted(divs)


for n in range(1820348, 2880927 + 1):
    d = div(n)

    if len(d) == 5:
        print(d[-1], d[-2])