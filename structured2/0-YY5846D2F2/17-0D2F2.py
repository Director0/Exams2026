f = open("17.txt")

nums = [int(x) for x in f]
sums = []
max17 = max([x for x in nums if len(str(abs(x))) == 5 and abs(x) % 100 == 17])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if any(abs(x) % 100 == 17 for x in ls) and sum([abs(x) for x in ls]) <= max17:
        sums.append(sum(ls))


print(len(sums))
print(min(sums))
