def div(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs


for k in range(1, 10**10):
    dvs = div((750_000 + k))

    if all(x % 2 == 0 for x in dvs) and len(dvs) % 2 != 0:
        print(k, len(dvs))