from re import *

s = open("24_18147.txt").read()

pat = r"[7-9]+[+](?:[7-9]+[+][7-9]+[+])*[7-9]+"

d = findall(pat, s)
rs = []

print(sorted(d, key=len))

for a in d:
    rs.append(sum(int(x) for x in a.split("+")))

print(sorted(rs))
print(max(rs))