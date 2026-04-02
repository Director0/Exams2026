from fnmatch import fnmatch


def dvs(n):
    divs = set()

    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            divs.add(d)
            divs.add(n // d)

    return divs or 0


for n in range(1, 10**7):
    if fnmatch(str(n), "31*567?") and dvs(n) == 0:
        sn = 1
        for x in str(n):
            sn *= int(x)

        print(n, sn)