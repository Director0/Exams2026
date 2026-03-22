s = open("24_21717.txt").read()

minl = 5000

for l in range(len(s)):
    for r in range(l + minl - 1, l, -1):
        d = s[l:r + 1]

        if d.count("RSQ") < 130:
            break

        if d.count("RSQ") == 130 and d[-1] != "Q":
            minl = min(minl, r - l + 1)


print(minl)