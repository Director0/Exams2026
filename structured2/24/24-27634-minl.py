s = open("24_27634.txt").read()

minl = 5000


for l in range(len(s)):
    for r in range(l + minl - 1, l, -1):
        d = s[l:r + 1]

        if d.count("Z") >= 270:
            minl = min(r - l + 1, minl)
            st = d
        else:
            break


print(minl, st)