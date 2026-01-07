def div_n8(n):
    divs = set()
    for i in range(1, int(n**0.5)):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return sum([x for x in divs if x % 10 == 8])


for n in range(114578, 114616):
    r = div_n8(n)
    print(r)

    # if r % 10 == 6:
    #     print(n, r)