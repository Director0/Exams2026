f = open("17_27301.txt")

nums = [int(x) for x in f]
sums = []
max45 = max([x for x in nums if str(abs(x))[:2] == "45"])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if x < 0]) == 1 and sum(ls) >= max45:
        sums.append(sum(ls))


print(len(sums))
print(min([x for x in sums if abs(x) % 100 == 45]))