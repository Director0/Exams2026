def simpl(n):
    res = []

    p = 2

    while p ** 2 <= n:
        if n % p == 0:
            res.append(p)
            n //= p
        else:
            p += 1

    if n > 1:
        res.append(n)

    return res


#//

for i in range(24517513, 10**10):
    s = simpl(i)

    if len(s) == 12:
        print(i, max(s))