from re import *

s = open("24_24895.txt").read()

pat = r"(?=([1-9]+(?:[+*][1-9]+){39}))"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))