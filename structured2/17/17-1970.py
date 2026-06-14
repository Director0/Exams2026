f = open("17_1970.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 1):
    ls = [nums[i], nums[i + 1]]

    if any(abs(x) % 3 == 0 for x in ls):
        sums.append(sum(ls))


print(len(sums))
print(max(sums))