from re import *

ls = []

s = open("24.txt").read()


for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    for y in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if x != y:
            pat = rf"(?:{x}{y})+{x}*"
            d = findall(pat, s)
            ls += d




print(ls)
print(max(ls, key=len))
print(len(max(ls, key=len)))