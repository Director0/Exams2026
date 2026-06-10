
def div(n):
    divs = set()

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs or {0}



for n in range(800_000, 10**9):
    divs = div(n)
    r1 = 1
    for x in divs:
        r1 *= x

    if sum(divs) % 2 != 0 and r1 % 2 != 0 and len(divs) > 10:
        print(n, len(divs))