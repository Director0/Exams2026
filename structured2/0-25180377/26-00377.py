f = open("26_8432.txt")

pka = [0] * 70
pkb = [0] * 30

bcn = 0
gcn = 0

for s in f:
    start, end, cls = list(map(int, s.split()))
    Ok = False

    if cls == 1:
        for i in range(len(pka)):
            if pka[i] <= start:
                pka[i] = end
                break
        else:
            for i in range(len(pkb)):
                if pkb[i] <= start:
                    pkb[i] = end
                    break

            else:
                gcn += 1


    elif cls == 2:
        for i in range(len(pkb)):
            if pkb[i] <= start:
                pkb[i] = end
                bcn += 1
                break
        else:
            gcn += 1


print(bcn)
print(gcn)
