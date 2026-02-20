s = open("24.txt").read()

maxl = 4
res = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if "Y" in d or "A" in d or "X" in d or d.count("E") != 2:
            break

        if d.count("E") == 2 and d[0] == "E" and d[-1] == "E":
            maxl = max(maxl, r - l + 1)
            res.append(d)

print(maxl, res)