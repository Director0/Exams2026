def smp(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True


def pr(n):
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


for n in range(12365266, 10**10):
    prm = pr(n)

    if len(prm) == 5 and len(prm) == len(set(prm)) and smp(sum(prm)) == True:
        print(n, sum(prm))