n = 0


def simp_n(n):
    res = []

    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            res.append(i)
            n //= i


        # divs.add(i)
        # divs.add(n // i)

    return res


for i in range(24517512, 100000000):
    f = simp_n(i)
    if len(f) == 12:
        print(i, max(f))