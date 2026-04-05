from re import *

s = open("24_28007.txt").read()

pat = r"(?:\((?:[1-9][0-9]*)?[12346789][+-](?:[1-9][0-9]*)?[05]\))+"

d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))
