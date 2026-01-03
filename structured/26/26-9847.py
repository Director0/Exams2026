f = open("26_9847.txt")

k = int(f.readline())
minutes = [0] * (24 * 60)

for i in range(k):
    beg, end = [int(k) for k in f.readline().split()]

    for g in range(beg, end):
        minutes[g] += 1

print(max(minutes))
res = []

for i in range(len(minutes)):
    if minutes[i] == max(minutes):
        res.append(i)

cnt1 = 0

for i in range(len(res) - 1):
    if abs(res[i] - res[i + 1]) > 1:
        cnt1 += 1

print(f"cnt: {cnt1 + 1}")
