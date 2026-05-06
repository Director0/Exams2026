
def smp(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

def prim(n):
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


for n in range(5_000_000, 10**9):
    pr = prim(n)

    if len(pr) == 2 and all(x % 2 != 0 for x in pr) and (pr[1] - pr[0]) != 0 and smp(pr[1] - pr[0]):
        print(n, max(pr))
