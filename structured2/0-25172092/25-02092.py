def div(n):
    divs = set()

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs or 0

print(div(5))

for n in range(3_333_338, 10**9):
    divs = div(n)
    smd = [x for x in divs if div(x) == 0]
    r = max(smd) - min(smd)

    if r > 1000 and r % 3 == 0:
        print(n ,r)