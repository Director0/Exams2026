f = open("17.txt")

nums = [int(x) for x in f]
sums = []


for i in range(len(nums) - 1):
    for j in range(i + 1, len(nums)):
        if abs((nums[i] - nums[j])) % 60 == 0:
            sums.append(abs(nums[i] - nums[j]))


print(sums)
print(len(sums))
print(max(sums))