f = open("17.txt")

nums = [int(x) for x in f]
sums = []
max23 = max([x for x in nums if x < 0 and abs(x) % 23 == 0])


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if (ls[0] != ls[1]) and (abs(ls[0] - ls[1]) % abs(max23) == 0):
        sums.append(abs(ls[0] - ls[1]))


print(len(sums))
print(min(sums))