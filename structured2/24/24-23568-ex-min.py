s = open("24_23568.txt").read()

for x in "0123456789":
    s = s.replace(x, "0")

maxl = 100
l1 = 0

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d[0].isdigit() or len(d) - d.count("0") > 2:
            break

        if d[0] == d[-1] and d[1:-1].isdigit():
            if len(d) > maxl:
                maxl = len(d)
                l1 = l


    if l % 100_000 == 0:
        print(l, maxl)


print(maxl)
print(l1) # с нуля