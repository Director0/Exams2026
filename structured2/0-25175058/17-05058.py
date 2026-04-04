f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min1 = min(nums)
max1 = max(nums)


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if (x % 3) == (min1 % 3)]) == 1 and len([x for x in ls if (x % 7) == (max1 % 7)]) >= 2:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))