f = open("26_5940.txt")

# 250
stat = {}

for l in f:
    ls = list(map(int, l.split()))

    stat[ls[0]] = [ls[1], ls[2]]


print(stat)
curr = 11
cntdist = 0

for sx in stat.keys():
    if sx == curr and (stat[sx + 1] in stat and stat[sx + 2] in stat):
        if stat[sx][0] < stat[sx][1]:
            curr = stat[sx + 1]
            cntdist += stat[sx][0]
        else:
            curr = stat[sx + 2]
            cntdist += stat[sx][1]

