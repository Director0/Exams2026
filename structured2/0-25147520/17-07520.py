f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
min0 = min([x for x in nums if x > 0])

for i in range(len(nums) - 3):
    ls = [nums[i], nums[i + 1], nums[i + 2], nums[i + 3]]

    if all(abs(x) % 111 != min0 for x in ls):
        sums.append(sum(ls))

print(sums)
print(len(sums))
print(min(sums))
print(min0)