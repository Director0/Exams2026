f = open("17_23757.txt")

nums = [int(x) for x in f]
n_min = min([x for x in nums if len(str(x)) == 2])
sums = []

for i in range(len(nums) - 1):
    if ((len(str(nums[i])) == 2) + (len(str(nums[i+1])) == 2) == 1) and (nums[i] + nums[i + 1]) % n_min == 0:
        sums.append(nums[i] + nums[i + 1])

print(len(sums))
print(max(sums))

