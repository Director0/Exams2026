def prim(n):
    ans = []
    d = 2

    while d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            if len(ans) > 2:
                return []
            n //= d
        else:
            d += 1

    ans.append(n)

    return ans


for n in range(7_513_048_000, 10**12):
    prs = prim(n)

    if len(prs) == 2 and all("1" in str(x) and str(x).count("6") == 1 for x in prs):
        print(n, max(prs))