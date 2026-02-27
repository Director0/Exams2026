from re import *

s = open("24.txt").read()

maxl = 10

for x in "KLMN":
    s = s.replace(x, "A")

for x in "123":
    s = s.replace(x, "x")

res = []
print(s)
for l in range(len(s)):
    for r in range(l + maxl, len(s)):
        d = s[l:r + 1]

        if d.count("A") > 2 * d.count("x") or d.count("A") < d.count("x"):
            break

        if d.count("A") == 2 * d.count("x"):
            maxl = max(maxl, r - l + 1)
            res.append(d)
            print(d, maxl)


print(maxl)
print(res)

# pat = r"(?:(?:[KLMN]{2})(?:[123]{1})|(?:[123]{1})(?:[KLMN]{2}))+"
# res = []
#
# for a in findall(pat, s):
#     if (a.count("K") + a.count("L") + a.count("M") + a.count("N")) == 2 * (a.count("1") + a.count("2") + a.count("3")):
#         res.append(a)
#
# print(res)
# print(max(res, key=len))
# print(len(max(res, key=len)))