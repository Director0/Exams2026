s = open("24_25361.txt").read()

maxl = 77
p1 = None

for l in range(0, len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d[0].isalpha() or d.count("F") > 76:
            break

        if d.count("F") == 76 and d[0].isdigit() and d[0] in "02468" and len([x for x in d if x in "02468"]) == 1:
            maxl = max(maxl, r - l + 1)
            print(d)

print(maxl)