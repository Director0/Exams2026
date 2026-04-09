from re import *

s = open("24.txt").read()

rs = []

for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    pat = fr"X+Z"
    rs += findall(pat, s)



print(sorted(rs, key=len, reverse=True))