import shlex

f = open("26_9756.txt")

k = int(f.readline())
t = [[int(x) for x in s.split()] for s in f]
t.sort(key=lambda x:x[0])
t.sort(key=lambda x:x[1])

cell = [[0,0]]
count = 0

for beg, end in t:
    if beg >= cell[-1][1]:
        count += 1
        cell.append([beg, end])

print(count, cell)

res = []

for s in t:
    if s[0] >= 991:
        res.append(s)

print(res)