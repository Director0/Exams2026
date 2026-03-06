f = open("17 (1).txt")

nums = [int(x) for x in f]
sums = []
min37 = min([x for x in nums if abs(x) % 37 == 0])
max73 = max([x for x in nums if abs(x) % 73 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if len([x for x in ls if min37 <= x <= max73]) == 1:
        sums.append(sum(ls))


print(len(sums))
print(min(sums))