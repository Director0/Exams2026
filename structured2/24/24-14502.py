s = open("24_14502.txt").read()

minl = 5000

for l in range(len(s)):
    for r in range(l + minl - 1, l, -1):
        d = set(s[l:r + 1])

        if len(d) == 26:
            minl = min(minl, r - l + 1)
        else:
            break

print(minl)