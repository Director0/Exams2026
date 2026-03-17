def smp(n):
    slm = []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            slm.append(i)

            n //= i

    if n != 1:
        slm.append(n)

    return slm

for n in range(2_000_000, 10**9):
    slm = smp(n)

    if len(slm) == 4 and len([x for x in slm if x > 600]) >= 2:
        print(n, max(slm))