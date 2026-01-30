f = open("26_3.txt")

# 998871

data = []
rs = []

for s in f:
    rm = list(map(int, s.split()))
    data.append(rm)


data.sort()
maxl = 0
curl = 1
linnum = 0
row = 0

for i in range(1, len(data)):
    if data[i][0] == data[i - 1][0]:
        if data[i][1] - data[i - 1][1] == 1:
            curl += 1
        elif data[i][1] - data[i - 1][1] > 1:
            if curl >= 4:
                linnum += 1
                if linnum >= maxl:
                    maxl = linnum
                    row = data[i][0]

            curl = 1

    else:
        if curl >= 4:
            linnum += 1
            if linnum >= maxl:
                maxl = linnum
                row = data[i - 1][0]

        curl = 1


print(maxl)
print(row)

