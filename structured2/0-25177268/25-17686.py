def div(n):
    divs = set()

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs or {0}


for n in range(700_000, 10**8):
    dvs = div(n)

    if any(str(x)[-1] == "7" and x != n and x != 7 for x in dvs):
        print(n, min([x for x in dvs if str(x)[-1] == "7" and x != n and x != 7]))