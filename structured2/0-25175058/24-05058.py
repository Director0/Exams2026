from re import *

s = open("24.txt").read()

pat = r"[1-9AB]+[0-9AB]*[13579B]"
rs = []

d = findall(pat, s)



print(max(d, key=len))

print(s.index("893061482509370741096528301876324059010753498260539406871201530842769061793402580475039182606107594238000A5"))