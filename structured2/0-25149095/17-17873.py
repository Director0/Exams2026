f = open("17_17873.txt")

nums = [int(x) for x in f]
sums = []
minl = min(nums)
cnt = 0

for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(x % 16 == minl for x in ls):
        sums.append(sum(ls))


print(sums)
print(len(sums))
print(max(sums))