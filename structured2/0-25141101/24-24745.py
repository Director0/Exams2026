from re import *

s = open("24_24745.txt").read()

s = s.replace("RR", "b").replace("LL", "b")
print(s)

maxl = 100000
res = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if "b" not in d or d[0] == "b" or d[-1] == "b" or d.count("b") < 100000:
            break

        if d.count("b") == 100000:
            maxl = max(maxl, r - l + 1)
            res.append(d)
        else:
            break


print(maxl)
print(res)