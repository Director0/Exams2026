
def div_n(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and div_n(i) == set():
            divs.add(i)

            if div_n(n // i) == set():
                divs.add(n // i)

    return divs

print(div_n(55000662))

for n in range(55_000_000, 100_000_000):
    pdvs = div_n(n)
    ns2 = [x for x in pdvs if str(x)[-3:] == "777" and x != n]

    if len(ns2) > 0:
        print(n, min(ns2))