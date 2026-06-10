f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
sum5 = sum([x for x in nums if abs(x) % 2 != 0 and len(str(abs(x))) == 5])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]
    r1 = 1

    if len([x for x in ls if abs(x) % 10 == abs(sum5) % 10]) == 1:
        for a in ls:
            r1 *= a
        sums.append(r1)


print(len(sums))
print(max(sums))