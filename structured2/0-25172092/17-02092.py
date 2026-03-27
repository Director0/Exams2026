f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
max01 = max([abs(x) for x in nums if abs(x) % 1001 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(len(str(abs(x))) == 3 for x in ls) and sum(ls) > max01:
        sums.append(sum(ls))


print(len(sums))
print(min(sums))