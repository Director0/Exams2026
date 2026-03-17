f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min1 = min([x for x in nums if x > 0])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]
    pt = ls[0] * ls[1] * ls[2]

    if any(abs(x) % min1 == 0 for x in ls) and str(pt)[-1] == "4":
        sums.append(pt)


print(len(sums))
print(abs(min(sums)))