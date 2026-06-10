def prm(n):
    ans = []
    d = 2

    while d**2 <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1

    ans.append(n)

    return ans


for n in range(125697, 125721 + 1):
    p1 = prm(n)

    if len(p1) == 2:
        print(p1[0], p1[1])