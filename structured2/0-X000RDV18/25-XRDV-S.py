def prim(n):
    ans = []
    d = 2

    while n > 1 and d**2 <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1

    if n != 1:
        ans.append(n)

    return ans

print(prim(1001))
def smp(n):
    divs = set()

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True



for n in range(8_007_494_999 + 1, 10**10, 2):
    pr = prim(n)

    if len(pr) > 1:
        m = pr[0] + pr[-1]

        if m > 80000 and str(m).count("567") == 1 and smp(m):
            print(n, m)