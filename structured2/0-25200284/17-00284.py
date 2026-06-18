f = open("17.txt")

nums = [int(x) for x in f]
sums = []
max15 = max([x for x in nums if abs(x) % 100 == 15])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if len(str(abs(x))) == 4]) == 1 and sum(ls) >= max15:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))