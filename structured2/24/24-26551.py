from re import *

s = open("24_26551.txt").read()

pat = r"[1-9A-D][0-9A-D]*[02468AC]+"

d = findall(pat, s)

print(d)
print(max(d, key=len))
print(len(max(d, key=len)))
