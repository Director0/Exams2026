from re import *

s = open("24_9791.txt").read()

pat = r"[1-9A-F][0-9A-F]*"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))