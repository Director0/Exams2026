n = 0

def dvsm(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)
            break

    return sum(divs)

for i in range(800000, 900000):
    m = dvsm(i)

    if str(m)[-1] == "4" and n < 5:
        print(i, m)
        n += 1