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