f = open("26_22605.txt")


data = []

for a in f:
    ls = list(map(int, a.split()))
    data.append(ls)


data.sort()
print(data)

mint = 10**21
scor = 0

for i in range(len(data) - 1):
    if data[i][0] == data[i + 1][0] and data[i][1] == data[i + 1][1]:
        if abs(data[i][2] - data[i + 1][2]) < mint:
            mint = abs(data[i][2] - data[i + 1][2])
            scor = data[i][0] + data[i][1]


print(scor)
print(mint)

