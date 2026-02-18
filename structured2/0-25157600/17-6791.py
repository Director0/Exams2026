f = open("17_6791.txt")

nums = [int(x) for x in f]
sums = []
min68 = min([x for x in nums if abs(x) % 100 == 68])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if (len([x for x in ls if abs(x) % 100 == 68]) == 1) and ((ls[0] ** 2 + ls[1] ** 2) >= (min68 ** 2)):
        sums.append(ls[0] ** 2 + ls[1] ** 2)


print(len(sums))
print(max(sums))