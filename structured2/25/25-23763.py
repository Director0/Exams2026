#a, b = map(int, input().split())
n = 0

def div_n(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs



for i in range(800000, 900000):
    if n == 5:
        break

    dvs = div_n(i)

    if len(dvs) > 1 and (max(dvs) + min(dvs)) % 10 == 4:
        print(i, max(dvs) + min(dvs), dvs)
        n += 1

