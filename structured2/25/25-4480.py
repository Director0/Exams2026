#a, b = map(int, input().split())
n = 0

def div_n(n):
    divs = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs



for i in range(800000, 900000):
    dvs = div_n(i)
    d1 = 1
    lst1 = []

    for i1 in dvs:
        d1 *= i1

    if len(dvs) > 10 and sum(dvs) % 2 != 0 and d1 % 2 != 0:
        print(i, len(dvs))
        lst1.append([i, len(dvs)])


print(sorted(lst1))

