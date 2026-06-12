from re import *

s = open("24.txt").read()

pat = r"(?:[1-9][0-9]{3}[.][0-9]+[&][1-9][0-9]{3}[.][0-9]+)+"

d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))