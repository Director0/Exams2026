from re import *


s = open("24_28943.txt").read()

pat = r"[BCDFGHJKLMNPQRSTVWXZ0-9]+[AEIOUY]"

d = set(findall(pat, s))
rs = []

for x in d:
    rs.append((x, x.count("20"), len(x)))

print(sorted([x for x in rs if x[1] == 26], key = len))