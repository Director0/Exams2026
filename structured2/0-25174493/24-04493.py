from re import *

s = open("24.3.txt").read()

pat = r"(?:[A-Z]){4}"

d = findall(pat, s)
rs = []

for x in d:
    if len(set(x)) == 2 and x[0] == x[1] == x[2]:
      rs.append(x[3])



cnt = [[rs.count(x), x] for x in set(rs)]

print(sorted(rs))
print(cnt)
print(max(cnt))