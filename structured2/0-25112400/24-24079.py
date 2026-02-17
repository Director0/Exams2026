from re import *

s = open("24_24079.txt").read()

pat = r"(?=(B[02-9C-Z]+A1A[02-9C-Z]+B))"
d = findall(pat, s)

print(min(d, key=len))
print(len(min(d, key=len)))