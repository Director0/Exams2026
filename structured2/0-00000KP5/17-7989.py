f = open("17-428.txt")

nums = [int(x) for x in f]
sums = []
min13 = [x for x in nums if abs(x) % 13 == 0][12]
min25 = [x for x in nums if abs(x) % 25 == 0][24]


for i in range(len(nums) - 2):
    ls = [nums[i], nums[i + 1], nums[i + 2]]

    if len([x for x in ls if len(str(abs(x))) == 3]) != 0 and len([x for x in ls if sum([int(a) for a in str(x)]) == sum([int(a) for a in str(min13)])]) <= 1 and len([x for x in ls if sum([int(a) for a in str(x)]) == sum([int(a) for a in str(min25)])]) >= 2:
        sums.append(sum(ls))


print(len(sums))
print(sum(sums) / len(sums))