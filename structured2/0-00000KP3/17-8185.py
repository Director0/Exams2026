f = open("17-433.txt")

nums = [int(x) for x in f]
sums = []
min15 = min([x for x in nums if len(str(abs(x))) == 3 and str(abs(x))[-2:] == "15"])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if (all(x > 0 for x in ls) or all(x < 0 for x in ls)) and ((min(ls) * max(ls)) > min15**2):
        sums.append(min(ls) * max(ls))


print(len(sums))
print(min(sums))