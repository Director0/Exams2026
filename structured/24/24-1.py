from string import ascii_uppercase

s = open("24.txt").read()
print(len(s))

s = "GBCHTMISOGNSPNGAONFABABABABABABABABABKEAKGJIKOBCBCBABABABABABABCBCBCBCBCBCBCBDBDBDABDSDABABABABFAJBCABCBASCJXBCBCBCBCBCBCBABABABABAKNOIFOICBABCBABABABABABABABABABDASPKGMERKVJGIOEMG"
res = []



maxl = 0

s = s.replace("AB", "*").replace("CB", "*")

for ltr in ascii_uppercase:
    s = s.replace(f"{ltr}*", f"{ltr} *")

for ltr in ascii_uppercase:
    s = s.replace(f"*{ltr}", f"* {ltr}")

s = s.split()

for a in s:
    if "*" in a:
        res.append(a)

print(s)
print(res)
print(len(max(res, key=len)))

# for l in range(len(s)):
#     for r in range(l + maxl, len(s)):
#         d = s[l:r + 1]
#
#         if d.count("AB")