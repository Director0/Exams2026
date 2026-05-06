s = open("24_28765.txt").read()

maxl = 0

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r+1]

        if d.count("BC") <= 180:
            maxl = max(maxl, r - l + 1)
            m = d
        else:
            break

print(maxl)