from re import *

s = open("24_6029.txt").read()

pat = r"(?:EF)+E?|(?:FE)+F?"
d = findall(pat, s)

print(max(d, key=len))
print(len(max(d, key=len)))