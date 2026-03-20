from re import *

s = open("24-358.txt").read()

pat = r"[02468][13579A-Z]+"

d = findall(pat, s)
rs = []

# print(sorted(d, key=len))

for a in d:
    if a.count("S") == 31:
        rs.append(a)

print(sorted(rs, key=len))
print(max(rs, key=len))
print(len(max(rs, key=len)))