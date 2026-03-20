f = open("17_8373 (1).txt")

nums = [int(x) for x in f]
sums = []
min2 = min([x for x in nums if abs(x) % 2 == 0])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 2]]

    if len([x for x in ls if x % 2 == 0]) == 1 and nums[i + 1] % min2 == 0:
        sums.append(sum(ls))




print(len(sums))
print(min(sums))















