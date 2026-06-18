f = open("17_29839.txt")

nums = [int(x) for x in f]
sums = []
max37 = max([x for x in nums if abs(x) % 100 == 37])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if len(str(abs(x))) == 3]) == 2 and (sum(ls) / 3) > 0 and (sum(ls) / 3) < max37:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))