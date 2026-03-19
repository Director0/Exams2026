f = open("17_8373 (1).txt")

nums = [int(x) for x in f]
sums = []
min2 = min([x for x in nums if abs(x) % 2 == 0])


for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        ls = [nums[i], nums[j]]

        if len([x for x in ls if x % 2 == 0]) == 1 and len([x for x in ls if x % min2 == 0]) == 1:
            sums.append(sum(ls))




print(len(sums))
print(min(sums))















