f = open("26_1.txt")

n = f.readline()
k = int(f.readline())

data = [list(map(int, a.split())) for a in f]
data.sort(key=lambda x:x[1])

print(data)

curr = 0
rs = []

for i in range(len(data)):
    if data[i][0] >= curr:
        curr = data[i][1]
        rs.append(data[i])

print(rs)
print(len(rs))

r1 = [x for x in data if x[0] > rs[-2][1]]

print(r1)
print(23 * k)