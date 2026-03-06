s = open("24.txt").read()

maxl = 0
r1 = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d.count("Y") <= 150:
            maxl = max(maxl, r - l + 1)
            r1.append(d)
        else:
            break


print(maxl)
print(r1)