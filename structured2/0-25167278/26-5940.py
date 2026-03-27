f = open("26_5940.txt")

# n = 250
stat = {}

for l in f:
    ls = list(map(int, l.split()))

    stat[ls[0]] = [ls[1], ls[2]]


print(stat)
curr = 11
cntdist = 0


while curr + 1 in stat or curr + 2 in stat:
    dmin = 10**19
    nxt = 0

    if curr + 1 in stat:
        dmin = stat[curr][0]
        nxt = curr + 1

    if curr + 2 in stat and stat[curr][1] < dmin:
        nxt = curr + 2
        dmin = stat[curr][1]

    cntdist += dmin
    curr = nxt

print(curr)
print(cntdist)



# for sx in stat.keys():
#     if sx == curr and (stat[sx + 1] in stat and stat[sx + 2] in stat):
#         if stat[sx][0] < stat[sx][1]:
#             curr = stat[sx + 1]
#             cntdist += stat[sx][0]
#         else:
#             curr = stat[sx + 2]
#             cntdist += stat[sx][1]

