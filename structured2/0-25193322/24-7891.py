s = open("24_7891.txt").read()


maxl = 3
rs = []

for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d[1:-1].count(d[0]) != 0:
            break

        if d[0] == d[-1] and d[1:-1].count(d[0]) == 0:
            maxl = max(maxl, len(d))
            rs.append((d, len(d)))

    if l % 100_000 == 0:
        print(l, maxl)

print(maxl)
print(rs)