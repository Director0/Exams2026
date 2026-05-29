f = open("17.txt")

nums = [int(x) for x in f]
sums = []
min1 = min(nums)


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(abs(x) % 117 == abs(min1) for x in ls):
        sums.append(sum(ls))


print(len(sums))
print(max(sums))