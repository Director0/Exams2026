f = open("17_28762.txt")

nums = [int(x) for x in f]
sums = []
min23 = min([x for x in nums if abs(x) % 23 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(x % min23 == 0 for x in ls):
        sums.append(sum(ls))


print(len(sums))
print(max(sums))