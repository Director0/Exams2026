

indx = []
ls = []

maxl = 0

s = open("24_29354.txt").read()

for i in range(len(s) - 2):
    if s[i:i + 2] == "BC":
        indx.append(i)


for i in range(len(indx) - 191):
    ls.append(len(s[indx[i]:indx[i + 191]]))

print(ls)

print(max(ls))