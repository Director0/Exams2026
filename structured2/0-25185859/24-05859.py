from re import *

s = open("24.txt").read()

for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    s = s.replace(x, " ")

# pat = r"[1-9]+[13579]"
#
# d = findall(pat, s)
#
d = s.split()

n = [int(x) for x in d]

print(min(n))