from re import *

s = open("24.txt").read()


rs = []


pat = fr"X[A-Z]Z"
d = findall(pat, s)
rs1 = {}

for x in d:
        if x[1] in rs1:
            rs1[x[1]] += 1
        else:
            rs1[x[1]] = 1


print(rs1)
print(max(rs1))