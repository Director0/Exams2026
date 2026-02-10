def simpl(n):
    slm = set()

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.add(i)

            n //= i

    if n != 1:
        slm.add(n)

    return slm

print(simpl(120000450))


for n in range(456_789, 1_000_000):
    m = 0
    divs = sorted(simpl(n))

    if len(divs) < 4:
        m = 0
    else:
        m = divs[0] + divs[1] + divs[-1] + divs[-2]

    if m % 114 == 39:
        print(n, m)
