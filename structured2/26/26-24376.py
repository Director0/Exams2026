f = open("26_24376.txt")

n = f.readline()

data = [list(map(int, a.split())) for a in f]
data.sort()

mo = data[1][0] - data[0][0] - 1
mo2 = mo


for i in range(1, len(data) - 1):
    if data[i][1] == 0:
        mo = max(mo, data[i + 1][0] - data[i - 1][0] - 1)
    else:
        mo = max(mo, data[i + 1][0] - data[i][0] - 1)

    mo2 = max(mo2, data[i + 1][0] - data[i][0] - 1)


print(mo2)
print(mo)
