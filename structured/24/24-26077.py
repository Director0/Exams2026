from re import *

s = open("24_25361.txt").read()

pat = r"[02468][^F02468]*(?:[F][^F02468]*){76}"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))