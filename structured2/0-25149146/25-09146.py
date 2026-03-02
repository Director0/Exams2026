def smpl(n):
    slm = set()

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.add(i)

            n //= i

    if n != 1:
        slm.add(n)

    return slm


for n in range(2_200_000, 10**9):
    slm = smpl(n)
    m = max(slm) + min(slm)

    if len(str(m)) == 5 and str(m) == reversed(str(m)):
        print(n, m)