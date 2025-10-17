f = open("26_1275.txt")
# 7100 970

datasum = 0

lst = sorted([int(x) for x in f])
datasave = []

for x in lst:
    if datasum < 710:
        datasum += x
        datasave.append(x)

print(datasum, len(lst) - len(datasave))


# INCORRECT ///////////////////////