
s = open("24.txt").read()

ls = []

for i in range(len(s) - 1):
    if s[i] == "A":
        ls.append(s[i + 1])


print(ls)

res = []

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    res.append((x, ls.count(x)))


print(sorted(res, key=lambda x:x[1], reverse=True))