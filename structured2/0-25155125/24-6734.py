s = open("24_6734.txt").read()

minl = 10**20

for l in range(len(s)):
    for r in range(l + 7, len(s)):
        d = s[l: r + 1]

        if "." not in d or d.count(".") > 7:
            break

        if d.count(".") == 7:
            minl = min(minl, r - l + 1)


print(minl)
print(d)