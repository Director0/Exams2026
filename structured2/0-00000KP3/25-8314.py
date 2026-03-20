def primes(n):
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

for n in range(5_000_000, 10**8):
    pr = primes(n)
    ipr = [x for x in pr if pr.count(x) == 5]

    if str(n)[-2:] == "12" and len(ipr) >= 1:
        print(n, min(ipr), pr)