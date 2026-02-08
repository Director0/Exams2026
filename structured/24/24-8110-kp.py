from re import *

s = open("24-337.txt").read()

pat = r"[1-9][0-9]*[05]|[5]"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))