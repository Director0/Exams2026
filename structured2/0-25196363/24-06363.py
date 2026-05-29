from re import *

s = open("24.txt").read()

rs = []

for x in "ABCDEFGHIJKLMNOPQRSTUVW":
    s = s.replace(x, " ")

s = s.split()

for s1 in s:
    if fullmatch(r"(?:XYZ)+", s1):
        rs.append(s1)

print(sorted(rs, key=len))
print(max(rs, key=len))
print(len(max(rs, key=len)))