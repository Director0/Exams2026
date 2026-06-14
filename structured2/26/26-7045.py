f = open("26_7045.txt")

n, plac = list(map(int, f.readline().split()))

data = [list(map(int, a.split())) for a in f]


for i in range(len(data)):
    data[i].append(data[i][0] + data[i][1] + max(data[i][2], data[i][3]))

# data.sort(key=lambda x:x[0], key=lambda x:x[4], reverse=True)

data = sorted(sorted(data, key=lambda x:x[0]), key=lambda x:x[4], reverse=True)

print(data)