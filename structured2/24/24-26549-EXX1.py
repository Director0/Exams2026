from re import *

indx = []
lx = []

s = open("24_26549.txt").read()


for i in range(len(s) - 4):
    if s[i:i + 4] == "2025":
        indx.append(i)


for i in range(len(indx) - 50):
    if s[indx[i]:indx[i + 50]].count("Y") >= 140:
        lx.append(len(s[indx[i]:indx[i + 50]]))


print(max(lx) + 3)
