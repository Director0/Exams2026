def div(n):
    divs = set()

    for p in range(2, round(n**0.5) + 1):
        if n % p == 0:
            divs.add(p)
            divs.add(n // p)

    return sorted(divs)


cnt = 0

for n in range(800000, 10**20):
    divs = div(n)

    if (max(divs) + min(divs)) % 10 == 4 and len(divs) > 0:
        print(n, max(divs) + min(divs))
        cnt +=1

        if cnt == 5:
            break


