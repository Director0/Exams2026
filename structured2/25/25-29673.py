n = 0

def div_n(n):
    divs = set()

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs

print(div_n(45))

for i in range(123456789, 223456789 + 1):

    if (i ** 0.5) % 1 == 0:
        divs = div_n(i)

        if len(divs) == 3:
            print(i, max(divs))