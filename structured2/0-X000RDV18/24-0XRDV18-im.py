from re import *

s = open("24_31129.txt").read()

num = r"(?:0|[1-9][0-9]*)"
pat = rf"{num}(?:[-*]{num})*"

d = findall(pat, s)

print(len(max(d, key=len)))