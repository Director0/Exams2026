s = open("24_26078.txt").read()

minl = 100


for l in range(len(s)):
    for r in range(l + minl, l, -1):
        d = s[l:r + 1]

        if d.count("W") < 90 or d.count("2025") < 110:
            break

        if d.count("2025") >= 110 and d.count("W") == 90:
            minl = min(minl, len(d))


    if l % 100_000 == 0:
        print(l, minl)


print(minl)