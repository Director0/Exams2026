s = open("24_29354.txt").read()

s = s.replace("BC", "*").replace("BC", "*").replace("BC", "*")

rs = []
maxl = 1

for l in range(0, len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d.count("*") == 190:
            rs.append(d)

print(rs)









