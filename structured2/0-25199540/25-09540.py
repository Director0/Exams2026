def div(n):
    divs = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs

mem = 0

for n in range(700_000, 10**9):
    divs = div(n)

    if len(divs) > mem:
        print(n, len(divs))
        mem = len(divs)