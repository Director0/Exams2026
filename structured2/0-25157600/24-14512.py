s = open("24_14512 (1).txt").read()


from re import *

pat = r"[18][ABC]+[18]"
res = []

d = findall(pat, s)

for l in d:
    if l.count("B") == l.count("C") and d[0] != d[-1]:
        res.append(l)

print(res)
print(len(max(res, key=len)))

#
# maxl = 2 + 2
# res = []
#
# for l in range(len(s)):
#     for r in range(l + maxl, len(s)):
#         d = s[l:r + 1]
#
#         if d[0].isdigit() and d[-1].isdigit() and d[0] != d[-1] and d.count("B") == d.count("C") and d.count("8") == 1 and d.count("1") == 1:
#             maxl = max(maxl, r - l + 1)
#             res.append(d)
#
#
# print(maxl, res)


