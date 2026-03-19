f = open("17_17636 (1).txt")

nums = [int(x) for x in f]
sums = []
max3 = max([x for x in nums if len(str(abs(x))) == 3 and str(abs(x))[-1] == "3"])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if any(str(abs(x))[-1] == "3" and len(str(abs(x))) == 3 for x in ls) and sum(ls) < max3:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))