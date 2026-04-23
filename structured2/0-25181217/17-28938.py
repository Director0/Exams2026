f = open("17_28938.txt")

nums = [int(x) for x in f]
sums = []
max28 = max([x for x in nums if abs(x) % 100 == 28])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if any(len(str(abs(x))) == 3 for x in ls) and 0 < (sum(ls) / len(ls)) < max28:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))
