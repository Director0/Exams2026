def simpl(n):
    slm = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.append(i)

            n //= i

    if n != 1:
        slm.append(n)

    return slm

for n in range(8_000_000, 10**8):
    slm = simpl(n)

    if n % 100 == 10 and len([x for x in slm if slm.count(x) > 1]) == 0:
        print(n, max(slm))

