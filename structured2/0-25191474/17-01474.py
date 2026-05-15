f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
rg = 0
am1 = sum(nums) / len(nums)


for i in range(2, len(nums) - 2):
    ls = [nums[i], nums[i + 1]]
    ls1 = [nums[i - 1], nums[i + 2]]

    if ls[0] * ls[1] > ls1[0] * ls1[1]:
        sums.append(sum(ls))

        if any(x > am1 for x in ls):
            rg += 1


print(max(sums))
print(rg)