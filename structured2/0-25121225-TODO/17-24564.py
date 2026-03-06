f = open("17_24564 (1).txt")

nums = [int(x) for x in f]
sums = []
min3 = min([x for x in nums if x > 0 and len(str(abs(x))) == 3])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if (len([x for x in ls if len(str(abs(x))) == 3]) == 1) and (sum(ls) % min3 == 0):
        sums.append(sum(ls))


print(len(sums))
print(max(sums))