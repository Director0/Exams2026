from itertools import permutations


def prm(n):
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


for n in range(20262026, 10**9):
    pr = prm(n)

    psm = {sum(p) for p in permutations(pr, 2)}

    if 2026 in psm:
        print(n, max(pr))