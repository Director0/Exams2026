
def smp(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def div(n):
    divs = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs


for n in range(5_000_040, 10_000_001, 180):
    divs = div(n)

    if 400 < len(divs) < 440:
        print(n, max([x for x in divs if smp(x)]))