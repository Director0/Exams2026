s = open("24_18284.txt").read()

maxl = 0
res = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if "L" in d in "O" in d and "V" in d and "E" in d:
            maxl = max(maxl, r - l + 1)
            res.append(d)
            print(d)


print(maxl)
print(res)