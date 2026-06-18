s = open("24.txt").read()


maxl = 54


for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if "R" not in d or "A" not in d:
            break

        if d.count("R") >= 2 and d.count("A") <= 3:
            maxl = max(maxl, len(d))
        else:
            break



print(maxl)