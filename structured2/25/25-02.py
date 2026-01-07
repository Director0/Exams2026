def ldiv(n):
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return len(divs)


for n in range(177000, 177300 + 1):
    sn1 = sum([int(x) for x in str(n)])

    if ldiv(n) == 2 and ldiv(sn1) == 2:
        print(n, sn1)


