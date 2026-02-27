def smpl(n):
    slm = set()

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.add(i)

            n //= i

    if n != 1:
        slm.add(n)

    return slm


for n in range(326_782, 965_324 + 1):
    slm = list(smpl(n))

    if (len(slm) == 3) and (slm[0] * slm[1] * slm[2] == n) and (max(slm) - min(slm) <= 12):
        print(n, max(slm) - min(slm))


