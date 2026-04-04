f = open("26.txt")

# 6000

rm = {}


for line in f:
    ls = list(map(int, line.split()))

    if ls[0] in rm:
        rm[ls[0]].add(ls[1])
    else:
        rm[ls[0]] = set()
        rm[ls[0]].add(ls[1])

print(rm)

mxs = 0

for x in rm.items():
    rsum = 0

    for i in range(len(x) - 1):
        if x[i] + 1 == x[i + 1]:
            rsum += 1
        else:
            break

    if rsum > mxs:
        mxs = rsum


print(mxs)