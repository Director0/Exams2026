def smpl(n):
    slm = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.append(i)

            n //= i

    if n != 1:
        slm.append(n)

    return slm


for n in range(2_142_577, 10**10):
    slm = smpl(n)

    if len(slm) == 2 and sum(slm) % 2 != 0:
        print(n, max(slm))