def prim(n):
    ans = []
    d = 2

    while d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1

    ans.append(n)

    return ans


for n in range(89427150 + 1, 10**9):
    slm = prim(n)
    xp = set(x for x in slm if slm.count(x) == 2)
    xnp = [x for x in slm if slm.count(x) == 1]

    if len(slm) == 8 and len(xp) == 2 and len(xnp) == 4 and min(slm) not in xp:
        print(n, max(slm))