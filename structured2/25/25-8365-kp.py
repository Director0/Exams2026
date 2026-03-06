def smp(n):
    slm = []

    for i in range(2, int(n**0.5) + 1):
        while n % i == 0:
            slm.append(i)

            n //= i

    if n != 1:
        slm.append(n)

    return slm

print(smp(75))

for n in range(700_001, 10**9):
    slm = smp(n)

    if len(slm) > 1 and len(set(slm)) == 1:
        print(n, slm[0])