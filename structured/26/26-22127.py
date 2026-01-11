f = open("26_22127.txt")

# 90000
ls = []
res = [1564, 349]

for s in f:
    ts, te = map(int, s.split())

    ls.append([ts, 1])
    ls.append([te, -1])

ls.sort(key=lambda x:x[1], reverse=True)
ls.sort(key=lambda x:x[0])


print(ls[-1])

curr = 0
for i in range(len(ls) - 1):
    l1, l2 = ls[i], ls[i + 1]
    curr += l1[1]

    if curr == 0:
        res.append(l2[0] - l1[0] - 1)

print(len(res))
print(sum(res))

