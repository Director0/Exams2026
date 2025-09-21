# UNVERSAL DEVISORS REFACTOR!! // S1NUMVB

# // Range Parameter
rang1, rang2 = map(int, input().split())

dev = []

# // Main
for n in range(rang1, rang2 + 1): # // Select num to num from rang

    for i in range(1, n + 1): # // Select dev to dev from range

        if n % i == 0: dev.append(i) # // Append selected dev

    # if len(dev) == 2:
    #     print(n)
    #     break

    print(dev)

    dev.clear() # // Prepare for next selection


# DIVISORS /////////////////////

a, b = map(int, input().split())

def div_n(n):
    divs = set()
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divs.add(i)
            divs.add(n // i)

    return len(divs)


for i in range(a, b+1):
    if div_n(i) == 4:
        print(i)