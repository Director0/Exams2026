f = open("26_12478.txt")
# 100000 1000 18000

st = 1000
en = 18000
ls = []
res = []

for s in f:
    ls.append(list(map(int, s.split())))

ls.sort()

tm = 0

for t1, t2 in ls:
    if t1 > st:
        st = tm
        res.append(tm)

    if t1 <= st and t2 > tm:
        tm = t2

    if tm > en:
        res.append(tm)
        break

print(len(res))
print(res)
print(res[0] - 1000)