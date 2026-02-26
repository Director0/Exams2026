f = open("17_25725 (1).txt")

nums = [int(x) for x in f]
sums = []
cnt3 = len([x for x in nums if abs(x) % 3 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if (len([x for x in ls if x < 0]) == 1) and (ls[ls.index([x for x in ls if x < 0][0]) - 1] % 2 == 0) and (sum(ls) > cnt3):
        sums.append(sum(ls))


print(len(sums))
print(max(sums))