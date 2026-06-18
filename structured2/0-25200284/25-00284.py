from fnmatch import fnmatch

def div(n):
    divs = set()

    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs


for n in range(217, 10**7, 217):
    if fnmatch(str(n), "14?4*"):
        divs = div(n)
        print(n, sum([x for x in divs if x % 2 != 0]))