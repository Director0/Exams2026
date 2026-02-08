from re import *

s = open("24-363.txt").read()

pat = r"(?=([1-9]+(?:[+*][1-9]+){79}))"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))