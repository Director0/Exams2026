def div(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs or {0}


for n in range(424_242, 10**10):
    divs = div(n)
    m = max(divs) + min(divs)

    if m % 2024 == 42:
        print(n, m)