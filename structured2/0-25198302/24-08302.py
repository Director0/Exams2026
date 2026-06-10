from re import *

s = open("24.txt").read()

pat = r"(?:[24][135])+"

d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))
