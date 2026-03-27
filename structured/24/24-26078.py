s = open("24_26078.txt").read()

minl = 5000

for l in range(len(s)):
    for r in range(l + minl - 1, l, -1):
        d = s[l:r + 1]

        if d.count("W") < 90 or d.count("2025") < 110:
            break

        if d.count("2025") >= 110 and d.count("W") == 90:
            minl = min(minl, r - l + 1)
            st = d


print(minl)