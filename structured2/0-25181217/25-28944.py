def prim(n):
    ans = []
    d = 2

    while d ** 2 <= n:
        if n % d == 0:
            ans.append(d)
            n//= d
        else:
            d += 1

    if n != 1:
        ans.append(n)

    return ans


for n in range(8_996_452, 10**9):
    p1 = prim(n)

    if len(p1) == 2 and all(str(x).count("3") == 2 for x in p1):
        print(n, max(p1))