
def smp(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

def div(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if smp(i):
                divs.add(i)
            if smp(n // i):
                divs.add(n // i)

    return divs or {0}


for n in range(23_600_000,  10**10):
    divs = div(n)
    m = max(divs) + min(divs)

    if m % 213 == 171:
        print(n, m)