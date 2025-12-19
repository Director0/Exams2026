n = 0

def simpl(n):
    slm = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            slm.append(i)

            n //= i

    if n != 1:
        slm.append(n)

    return slm


for i in range(13475124, 40000000):
    ms = simpl(i)

    if (len(ms) == 5 and all(str(v).count("5") >= 1 for v in ms)) and (n < 5):
        print(i, max(ms))

        n += 1