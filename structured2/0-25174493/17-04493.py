f = open("17 (1).txt")

nums = [int(x) for x in f]
sxms = []

for x in nums:
    if x % 5 == 3 and x % 9 == 5 and x % 8 != 7:
        sxms.append(x)


print(len(sxms))
print(max(sxms))