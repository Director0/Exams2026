s = open("24.txt").read()

maxl = 515616516851651651519156178918891651
res = []

for l in range(len(s)):
    for r in range(l + 9, len(s)):
        d = s[l:r + 1]

        if d.count("FAT") + d.count("BAD") < 3 or d.count("FAT") + d.count("BAD") > 3:
            break

        if d.count("FAT") + d.count("BAD") == 3:
            maxl = min(maxl, r - l + 1)
            st = d

print(maxl, st)