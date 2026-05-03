f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
cnt2 = len([x for x in nums if len(str(abs(x))) == 2])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if sum(int(str(x)[-1]) for x in ls) == cnt2:
        sums.append(sum(ls))


print(len(sums))
print(min(sums))