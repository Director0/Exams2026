def div(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs or 0


for n in range(600_000, 10**8):
    if n % 6 == 0 and div(n + 1) == 0 and div(n - 1) == 0:
        print(n - 1, n + 1)