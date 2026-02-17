s = open("24.txt").read()
#
# maxl = 10
# res = []
#
# for l in range(len(s)):
#     for r in range(l + maxl, len(s)):
#         d = s[l:r + 1]
#
#         if "ad" in d:
#             break
#
#         if "ad" not in d:
#             maxl = max(maxl, r - l + 1)
#             st = d
#
# print(maxl, st) NO

s = s.replace("ad", "a d").replace("da", "d a").split()

print(max(s, key=len))
print(len(max(s, key=len)))