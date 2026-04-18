def div(n):
    divs = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)


    return divs


print(div(5))


for n in range((5_000_000 // 360) * 360, 10_000_000, 360):
    dvs = div(n)

    if n % 360 == 0 and 400 < len(dvs) < 440:
        print(n, max([x for x in dvs if len(div(x)) == 2]))