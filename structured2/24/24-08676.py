s = open("24 (1).txt").read()

for x in "13579":
    s = s.replace(x, "*")


# print(s.count("2022"))

# minl = 700000
# l1 = 0

# for l in range(len(s)):
#     for r in range(l + minl, l, -1):
#         d = s[l:r + 1]
#
#         if d.count("*") < 2008 or d.count("2022") < 2026:
#             break
#
#         if d.count("2022") >= 2026 and d.count("*") == 2008:
#             if len(d) < minl:
#                 minl = len(d)
#                 l1 = l
#
#
#     if l % 100_000 == 0:
#         print(l, minl)
#
#
# print(minl)
# print(l1)

# indx = []
# milx = []
#
# for i in range(len(s)):
#     if s[i] == "*":
#         indx.append(i)
#
#
# for i in range(len(indx) - 2008):
#     if s[indx[i]:indx[i + 2008]].count("2022") == 2026:
#         milx.append(len(s[indx[i]:indx[i + 2008]]))
#
#
# print(min(milx))

s = s.split("*")
ls = []

for a in s:
    ls.append(a.count("2022"))


for i in range(len(ls) - 2490):
    if sum(ls[i:i + 2490]) >= 2026:
        print(i)