f = open("17.txt")

nums = [int(x) for x in f]
sums = []
max4 = max([x for x in nums if len(str(abs(x))) == 4])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if abs(ls[0] - ls[1]) >= max4:
        sums.append(sum(ls))


print(len(sums))
print(max(sums))