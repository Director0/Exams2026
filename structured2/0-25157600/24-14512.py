s = open("24_14512 (1).txt").read()

maxl = 1
res = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d[0] == d[-1] or d[0].isalpha() or d[-1].isalpha():
            break

        if d[0].isdigit() and d[-1].isdigit() and d[0] != d[-1] and d.count("B") == d.count("C") and d.count("8") == 1 and d.count("1") == 1:
            maxl = max(maxl, r - l + 1)
            res.append(d)

print(maxl, res)
print(s.index('8AAACBACABBCBBCCCB1'))