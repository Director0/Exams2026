def prim(n):
    ans = []
    d = 2

    while n > 1 and d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1

    if n != 1:
        ans.append(n)

    return ans


for n in range(3_909_600, 10**9):
    slm = sorted(prim(n))

    if len(slm) == 7 and slm[-1] > sum([x for x in slm if x != slm[-1]]):
        print(n, slm[-1])

