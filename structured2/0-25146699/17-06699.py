f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
max3 = max([x for x in nums if x % 10 == 3 and len(str(abs(x))) == 3])
cnt = 0

for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if (len([x for x in ls if x % 10 == 3 and len(str(abs(x))) == 3]) >= 1) and (sum(ls) < max3):
        sums.append(sum(ls))


print(sums)

print(len(sums))
print(max(sums))