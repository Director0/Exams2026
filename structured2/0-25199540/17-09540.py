f = open("17.txt")

nums = [int(x) for x in f]
sums = []
smx = []


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if abs(x) % 40 == 15]) == 2 and len([x for x in ls if abs(x) % 7 == 0]) <= 2:
        sums.append(sum(ls))
        smx.append([x for x in ls if abs(x) % 40 != 15][0])


print(len(sums))
print(sum(smx))