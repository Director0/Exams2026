f = open("17.txt")

nums = [int(x) for x in f]
sums = []


for n in nums:
    for g in nums:
        if abs((n - g)) % 60 == 0:
            sums.append(abs(n - g))


print(sums)
print(len(sums))
print(max(sums))