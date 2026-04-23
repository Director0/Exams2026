f = open("17.txt")

nums = [int(x) for x in f]
sums = []
max18 = max([x for x in nums if abs(x) % 100 == 18])


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]
    nx = 1

    for x in ls:
        nx *= x

    if any(len(str(abs(x))) == 5 for x in ls) and nx % max18 == 0:
        sums.append(nx)


print(len(sums))
print(max(sums))