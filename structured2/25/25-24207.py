n = 0

def div_n(n):
    divs = set()

    for i in range(n, int(n ** 0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return divs


for i in range(24517512, ):
    print(0)
