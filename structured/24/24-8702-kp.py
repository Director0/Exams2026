s = open("24-367.txt").read()

minl = 10 ** 10
k = 0
l = s.index(".A") + 1

for r in range(l - 1, len(s) - 1):
    # if k < 600:
    if s[r] == "." and s[r + 1] == "A":
        k += 1

    if k == 600 and s[r + 1] == ".":
        minl = min(minl, r - l + 3) # (+2)

    if k > 600:
        l += 1

        while not(s[l - 1] == "." and s[l] == "A"):
            l +=1

        k -= 1

print(minl)

# 2cycles

