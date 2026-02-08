from re import *

s = open("24-345.txt").read()

pat1 = r"[1-9A-D][0-9A-D]*[02468AC]|[02468AC]"

d1 = findall(pat1, s)

print(d1)
print(len([x for x in d1 if len(x) == 112]))

max2 = max(d1, key=len)
print(max2)

print(s.index(max2))
