from re import *

s = open("24_3019.txt").read()

pat = r"A(?:[^AB])*B"

d = findall(pat, s)
rs = []

print(d)

for a in d:
    if len(a) <= 15 and "F" in a:
        rs.append(a)


print(rs)
print(len(rs))