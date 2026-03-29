f = open("26-ikk.txt")

# 82729

data = []

for a in f:
    ls = list(map(int, a.split()))
    data.append(ls)


data.sort()
data.append([100000, 100000, 0])

decsum = 0
mxsum = 0
mxid = 0
currsum = 0

for i in range(len(data) - 1):
    if data[i][0] != data[i + 1][0]:
        if currsum > mxsum:
            mxsum = currsum
            mxid = data[i][0]

        currsum = 0

    elif data[i][1] != data[i + 1][1]:
        currsum += data[i][2]

    else:
        decsum += data[i][2]


print(mxid)
print(decsum)
